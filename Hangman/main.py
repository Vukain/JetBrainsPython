import random
import string


def printer(_word, _setic):
    print("\n")
    for letter in _word:
        print(letter if letter in _setic else "-", end="")
    print()


def menu():
    while True:
        pl = input('Type "play" to play the game, "exit" to quit: ')
        if pl == "play":
            return True
        elif pl == "exit":
            return False

def game():
    hit_letters = set()
    missed_letters = []
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    tries = 8

    while tries > 0:
        printer(word, hit_letters)
        n = input(f"Input a letter: ")

        if len(n) != 1:
            print("You should input a single letter")
            continue
        elif n not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue

        if n in word:
            if n not in hit_letters:
                hit_letters.add(n)
            else:
                print("You already typed this letter")
                continue
        elif n in missed_letters:
            print("You already typed this letter")
        else:
            print("No such letter in the word")
            missed_letters.append(n)
            tries -= 1

        if len(hit_letters) == len(word):
            print(f"You guessed the {word}!\nYou survived!")
            break

    else:
        print("You are hanged!\n")


print("""H A N G M A N""")
playing = menu()

while playing:
    game()
    playing = menu()