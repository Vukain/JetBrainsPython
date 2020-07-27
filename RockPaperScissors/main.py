import random


play = True
name = input("Enter your name: ")
print(f"Hello, {name}")
user_combo = input()
combinations = user_combo.split(",") if user_combo != "" else ["rock", "paper", "scissors"]
score = 0
print("Okay, let's start")

file = open("rating.txt")
for line in file:
    if name in line:
        score = line.split(" ")[1]

while play:
    user_choice = input()
    computer_choice = random.choice(combinations)

    if user_choice == "!rating":
        print(f"Your rating: {score}")
        continue
    elif user_choice == "!exit":
        print("Bye!")
        play = False
        break

    if user_choice in combinations:
        combo = combinations[combinations.index(user_choice) + 1:] + combinations[:combinations.index(user_choice)]
        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        elif computer_choice in combo[int(len(combo) / 2):]:
            print(f"Well done. Computer chose {computer_choice} and failed")
            score += 100
        elif computer_choice in combo[:int(len(combo) / 2)]:
            print(f"Sorry, but computer chose {computer_choice}")
    else:
        print("Invalid input")