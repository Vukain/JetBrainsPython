class CoffeeMachine:

    def __init__(self):
        self.resources = {"water": 400, "milk": 540, "beans": 120, "disposable cups": 9, "money": 550}
        self.espresso = {"water": 250, "milk": 0, "beans": 16, "disposable cups": 1, "money": 4}
        self.latte = {"water": 350, "milk": 75, "beans": 20, "disposable cups": 1, "money": 7}
        self.cappuccino = {"water": 200, "milk": 100, "beans": 12, "disposable cups": 1, "money": 6}
        self.state = "main"
        self.working = True

    def status(self):
        print(f"""The coffee machine has:
    {self.resources['water']} of water
    {self.resources['milk']} of milk
    {self.resources['beans']} of coffee beans
    {self.resources['disposable cups']} of disposable cups
    {self.resources['money']} of money
    """)

    def buyer(self, coffee_type):
        for key in list(coffee_type.keys())[:-1]:
            if coffee_type[key] > self.resources[key]:
                print(f"Sorry, not enough {key}")
                break
        else:
            print("I have enough resources, making you a coffee!")
            for key in coffee_type.keys():
                if key == "money":
                    self.resources[key] += coffee_type[key]
                else:
                    self.resources[key] -= coffee_type[key]

    def picker(self, order):
        if order == "1":
            coffee = self.espresso
        elif order == "2":
            coffee = self.latte
        else:
            coffee = self.cappuccino
        self.buyer(coffee)

    def filler(self, order):
        if "water" in self.state:
            self.resources["water"] += int(order)
            self.state = "filling milk"
        elif "milk" in self.state:
            self.resources["milk"] += int(order)
            self.state = "filling beans"
        elif "beans" in self.state:
            self.resources["beans"] += int(order)
            self.state = "filling cups"
        elif "cups" in self.state:
            self.resources["disposable cups"] += int(order)
            self.state = "main"

    @staticmethod
    def listening():
        command = input()
        return command

    def using(self):
        while self.working:
            if self.state == "main":
                print("Write action (buy, fill, take, remaining, exit): ")
                cmd = self.listening()
                if cmd == "buy":
                    self.state = "buying"
                elif cmd == "fill":
                    self.state = "filling water"
                elif cmd == "take":
                    print(f"I gave you ${self.resources['money']}")
                    self.resources['money'] = 0
                elif cmd == "remaining":
                    self.status()
                elif cmd == "exit":
                    self.working = False
                else:
                    print("Unrecognized command")
            elif self.state == "buying":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
                cmd = self.listening()
                if cmd == "back":
                    self.state = "main"
                else:
                    self.picker(cmd)
                    self.state = "main"
            else:
                if "water" in self.state:
                    print("Write how many ml of water do you want to add: ")
                elif "milk" in self.state:
                    print("Write how many ml of milk do you want to add: ")
                elif "beans" in self.state:
                    print("Write how many grams of coffee beans do you want to add: ")
                else:
                    print("Write how many disposable cups of coffee do you want to add: ")
                cmd = self.listening()
                self.filler(cmd)


cafroboto = CoffeeMachine()
cafroboto.using()
