import string


class Calculator:
    variabs = dict()

    def __init__(self):
        pass

    def take_cmd(self):
        while True:
            choice = input()
            if choice.startswith("/"):
                if choice == "/exit":
                    print("Bye!")
                    break
                elif choice == "/help":
                    print("The program calculates the sum of numbers")
                else:
                    print("Unknown command")
            elif choice == "":
                continue

            elif "=" in choice:
                if choice.count("=") > 1:
                    print("Invalid assignment")
                    continue
                else:
                    modified = choice.replace(" ", "")
                    lis = modified.split("=")
                    for letter in lis[0]:
                        if letter.lower() not in string.ascii_lowercase:
                            print("Invalid identifier")
                            break
                    else:
                        if lis[1].isnumeric():
                            Calculator.variabs[lis[0]] = lis[1]
                        else:
                            try:
                                Calculator.variabs[lis[0]] = Calculator.variabs[lis[1]]
                            except:
                                print("Invalid assignment")
            else:
                modified = choice.replace(" ", "")

                self.calculate(modified)

    def calculate(self, expression):
        expre2 = f""
        for sign in expression:
            if sign in Calculator.variabs.keys():
                expre2 += str(Calculator.variabs[sign])
            else:
                expre2 += sign
        try:
            if "//" in expression or "**" in expression:
                raise ValueError
            print(int(eval(expre2)))
        except:
            try:
                print(Calculator.variabs[expression])
            except:
                if expression.isalpha():
                    print("Unknown Variable")
                else:
                    print('Invalid expression')


calc = Calculator()
calc.take_cmd()