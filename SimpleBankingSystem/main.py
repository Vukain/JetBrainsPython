import random
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')


class Banking:
    cards = {}
    card_num = 0
    prefix = "400000"

    def __init__(self):
        self.number = Banking.create_card()
        self.pin = Banking.generator(4)
        self.balance = 0
        Banking.cards[self.number] = self
        Banking.card_num += 1
        cur.execute(f'INSERT INTO card(id, number, pin, balance) VALUES ({Banking.card_num}, {self.number}, {self.pin}, {self.balance})')
        conn.commit()
        
    @staticmethod
    def generator(n):
        return "".join([str(random.randint(0, 9)) for i in range(n)])

    @staticmethod
    def luhn(numba):
        numbers = list(map(int, numba))
        numbers_x2 = [(e * 2) if i % 2 == 0 else e for i, e in enumerate(numbers)]
        numbers_minus = [e if e < 10 else e - 9 for e in numbers_x2]
        numbers_sum = sum(numbers_minus)
        for i in range(10):
            if (numbers_sum + i) % 10 == 0:
                return str(i)

    @classmethod
    def create_card(cls):
        main_part = cls.prefix + cls.generator(9)
        control = cls.luhn(main_part)
        return main_part + control

    @classmethod
    def menu(cls):
        using = True
        while using:
            print("""1. Create an account
2. Log into account
0. Exit""")

            cmd = input()
            if cmd == "0":
                print("Bye!")
                break
            elif cmd == "1":
                tmp = Banking()
                print(f"""Your card has been created
Your card number:
{tmp.number}
Your card PIN:
{tmp.pin}""")
            elif cmd == "2":
                crd = input("Enter your card number:\n")
                pn = input("Enter your PIN:")
                if crd not in cls.cards or cls.cards[crd].pin != pn:
                    print("Wrong card number or PIN!")
                else:
                    print("You have successfully logged in!")
                    while True:
                        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1""")
                        cmd = input()
                        if cmd == "1":
                            blc = cur.execute(f'SELECT balance FROM card WHERE number = {crd}').fetchone()
                            conn.commit()
                            print(f"Balance: {blc}")

                        elif cmd == "2":
                            inc = input("Enter income: \n")
                            cur.execute(f'UPDATE card SET balance = balance + {inc} WHERE number = {crd}')
                            conn.commit()
                            print("Income was added!")

                        elif cmd == "3":
                            print('Transfer')
                            print(cur.execute('SELECT number FROM card').fetchall())
                            tran_num = input('Enter card number: \n')
                            
                            if tran_num == tran_num[:-1] + Banking.luhn(tran_num[:-1]):

                                if (tran_num,) not in cur.execute('SELECT number FROM card').fetchall():
                                    print('Such a card does not exist.')
                                elif tran_num == crd:
                                    print("You can't transfer money to the same account!")
                                else:
                                    tran_money = int(input('Enter how much money you want to transfer: \n'))
                                    print(cur.execute(f'SELECT balance FROM card WHERE number = {crd};').fetchone()[0])
                                    blc = cur.execute(f'SELECT balance FROM card WHERE number = {crd};').fetchone()[0]
                                    if tran_money > int(blc):
                                        print("Not enough money!")
                                    else:
                                        cur.execute(
                                            f'UPDATE card SET balance = balance - {tran_money} WHERE number = {crd}')
                                        cur.execute(
                                            f'UPDATE card SET balance = balance + {tran_money} WHERE number = {tran_num}')
                                        conn.commit()
                            else:
                                print('Probably you made mistake in the card number. Please try again!')

                        elif cmd == "4":
                            cur.execute(f'DELETE FROM card WHERE number = {crd}')
                            conn.commit()
                            print("The account has been closed!")
                            break

                        elif cmd == "5":
                            break

                        elif cmd == "0":
                            using = False
                            print("Bye!")
                            break


Banking.menu()
