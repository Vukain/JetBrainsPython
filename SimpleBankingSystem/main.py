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
2. Log out
0. Exit
>1""")
                        cmd = input()
                        if cmd == "1":
                            print(f"Balance: {cls.cards[crd].balance}")
                        elif cmd == "2":
                            break
                        elif cmd == "0":
                            using = False
                            print("Bye!")
                            break


Banking.menu()
conn.commit()
