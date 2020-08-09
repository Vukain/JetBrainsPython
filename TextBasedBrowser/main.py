import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

init()

if len(sys.argv) > 1:
    path = sys.argv[1]
    try:
        os.mkdir(path)
    except:
        pass
history = []


def url_check(url):
    if "https://" not in url:
        url = "https://" + url
    return url


def get_content(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    cont = ['p', 'h', 'ul', 'ol', 'li', 'a']

    content = soup.find_all(cont)
    site_content = [Fore.BLUE + link.text + Style.RESET_ALL if link.name == 'a' else link.text for link in content]

    return site_content


def browsing():
    while True:
        inp = input()

        if inp == "exit":
            break
        elif inp == "back":
            history.pop()
            print(history[-1].text if len(history) > 0 else "")
        elif "." in inp:
            url = url_check(inp)
            try:
                pager = requests.get(url)
                site = get_content(pager)
                for para in site:
                    print(para)
                with open(path + "//" + inp[:inp.index('.')] + ".txt", 'w') as page:
                    for para in site:
                        page.write(para)
                history.append(pager)
            except:
                print("Error")
        else:
            try:
                with open(path + "//" + inp + ".txt", 'r') as page:
                    pag = page.read()
                    print(pag)
            except:
                print("Error: Incorrect URL")


browsing()
