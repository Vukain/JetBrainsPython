import requests
import sys
from bs4 import BeautifulSoup


class Translator:

    def __init__(self):
        self.languages = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French", 6: "Hebrew",
                          7: "Japanese", 8: "Dutch", 9: "Polish", 10: "Portuguese", 11: "Romanian", 12: "Russian",
                          13: "Turkish"}
        self.mode = "single"
        self.translation = ""
        self.native_language = ""
        self.foreign_language = "english"

    def saver(self):
        with open(f'{self.word}.txt', "w") as file:
            file.write(self.translation)

    def printer(self):
        print(self.translation)

    def get_lang(self):
        print("Hello, you're welcome to the translator. Translator supports:")
        for k, v in self.languages.items():
            print(f"{k}. {v}")

        print("Type the number of your language:")
        lang = int(input())
        self.native_language = self.languages[lang]

        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        choice = int(input())
        if choice != 0:
            self.foreign_language = self.languages[choice]
        else:
            self.mode = "multi"

    def get_word(self):
        print("Type the word you want to translate:")
        self.word = input()

    def get_data(self):
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

        if self.foreign_language.capitalize() not in self.languages.values():
            raise Exception(
                f"Sorry, the program doesn't support {self.foreign_language}")

        n = 5 if self.mode == "single" else 1
        languages = list(filter(lambda x: x != self.native_language, self.languages.values())) if self.mode == "multi"
        else [self.foreign_language]

        for lang in languages:
            direction = f'{self.native_language.lower()}-{lang.lower()}'
            address = f'https://context.reverso.net/translation/{direction}/{self.word}'
            response = requests.get(address, headers=headers)

            if response.status_code == 404:
                raise Exception(f"Sorry, unable to find {self.word}")

            if response.status_code != 200:
                raise Exception(
                    "Something wrong with your internet connection")

            soup = BeautifulSoup(response.content, 'html.parser')

            words = soup.find_all('a', class_='translation')
            sentences = soup.find_all('div', class_='example')
            word_list = [word.text.strip() for word in words[1:n+1]]
            sentence_list = [sentence.text.strip().replace(
                '\n\n\n\n\n          ', ':\n') for sentence in sentences[:n]]

            self.translation += f'\n{lang} Translations:\n' + "\n".join(word_list) + "\n\n" + f'{lang} Examples:\n' +\
                                "\n\n".join(sentence_list) + "\n"

        self.saver()
        self.printer()

    def get_translation(self):
        self.get_lang()
        self.get_word()
        self.get_data()

    def cmd_translation(self):
        self.native_language = sys.argv[1]
        if sys.argv[2] == "all":
            self.mode = "multi"
        else:
            self.foreign_language = sys.argv[2]
        self.word = sys.argv[3]

        try:
            self.get_data()
        except Exception as e:
            print(e)


translator = Translator()
if len(sys.argv) == 1 or __name__ == "__main__":
    translator.get_translation()
else:
    translator.cmd_translation()
