# Ryan Simmons
# Simple banking system
# Implementation of SQLite
#


class Banking:
    from random import randint
    import sys

    def __init__(self):

        import sqlite3

        self.log_in = True
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
        self.conn.commit()

    def account_creation(self):

        while True:

            n_account = '400000'    # ALL accounts @ JETBRAINS_BANK have these first 6 digits
            n_pin = ''
            total = 0
            is_luhn = False
            account_check = None

            for _ in range(10):
                n_account += str(self.randint(0, 9))

            for i in range(16):     # Checking if generated number is LUHN
                x = int(n_account[i])
                if i % 2 == 0:
                    x *= 2
                if x > 9:
                    x -= 9
                total += x
            if total % 10 == 0:     # If it is LUHN, it then checks to see if account already exists in DB
                is_luhn = True
                self.cur.execute('SELECT number FROM card WHERE number=?', (n_account,))
                account_check = self.cur.fetchone()
                self.conn.commit()
                self.conn.commit()

            if is_luhn and not account_check:   # Valid new account; LUHN and not already in DB
                for _ in range(4):
                    n_pin += str(self.randint(0, 9))

                self.cur.execute('INSERT INTO card(number, pin) VALUES (?,?)', (n_account, n_pin))
                self.conn.commit()
                print('Your card has been created', 'Your card number:', n_account, 'Your card PIN:', n_pin, '', sep='\n')
                break

    def account_login(self):

        account = input('Enter your card number: ')
        pin = input('Enter your PIN: ')

        self.cur.execute('SELECT * FROM card WHERE number=?', (account,))
        account_info = self.cur.fetchone()
        self.conn.commit()

        if account_info is None:
            print('', 'Wrong card number or PIN!', '', sep='\n')  # Account doesn't exist in DB
        else:
            if pin in account_info:
                print('', 'You have successfully logged in!', '', sep='\n')   # Account exists and pin matches
                self.account_menu(account)
            elif pin not in account_info:
                print('', 'Wrong card number or PIN!', '', sep='\n')  # Account exists but pin does not match

    def account_deposit(self, account_info):

        deposit = int(input('\nEnter income: '))

        self.cur.execute('UPDATE card SET balance=? WHERE number=?', (account_info[3] + deposit, account_info[1]))
        self.conn.commit()
        print('Income was added!\n')

    def account_transfer(self, account_info):

        is_luhn = False
        total = 0

        print('Transfer')
        t_account = input('Enter card number: ')

        if t_account == account_info[1]:
            print("You can't transfer money to the same account!")
        else:
            for i in range(16):     # Checking if transfer number is LUHN
                x = int(t_account[i])
                if i % 2 == 0:
                    x *= 2
                if x > 9:
                    x -= 9
                total += x
            if total % 10 == 0:
                is_luhn = True

            if not is_luhn:
                print('Probably you made mistake in the card number. Please try again!')
            else:
                self.cur.execute('SELECT * FROM card WHERE number=?', (t_account,))
                t_account_info = self.cur.fetchone()
                self.conn.commit()

                if t_account_info is None:
                    print('Such a card does not exist.')
                else:
                    transfer = int(input('Enter how much money you want to transfer:'))
                    if account_info[3] < transfer:
                        print('Not enough money')
                    else:
                        self.cur.execute('UPDATE card SET balance=? WHERE number=?', (account_info[3] - transfer, account_info[1]))
                        self.conn.commit()
                        self.cur.execute('UPDATE card SET balance=? WHERE number=?', (t_account_info[3] + transfer, t_account_info[1]))
                        self.conn.commit()
                        print('Success!\n')

    def account_close(self, account):

        self.cur.execute('DELETE FROM card WHERE number=?', (account,))
        self.conn.commit()
        print('', 'The account has been closed!', '', sep='\n')

    def account_menu(self, account):

        while self.log_in:

            self.cur.execute('SELECT * FROM card WHERE number=?', (account,))       # Grabbing most recent info on the account
            account_info = self.cur.fetchone()
            self.conn.commit()

            print('1. Balance', '2. Add income', '3. Do transfer', '4. Close account', '5. Log out', '0. Exit', sep='\n')
            menu_2 = input()
            if menu_2 == '0':
                self.exit()
                break
            elif menu_2 == '1':
                print('', f'Balance: {account_info[3]}', '', sep='\n')
                continue
            elif menu_2 == '2':
                self.account_deposit(account_info)
            elif menu_2 == '3':
                self.account_transfer(account_info)
            elif menu_2 == '4':
                self.account_close(account)
                self.log_in = False
            elif menu_2 == '5':
                print('', 'You have successfully logged out!', '', sep='\n')
                self.log_in = False

    def main_menu(self):    # MAIN LOOP

        while True:
            print('1. Create an Account', '2. Log into account', '0. Exit', sep='\n')
            menu_1 = input()
            print()

            if menu_1 == '0':
                self.exit()
            elif menu_1 == '1':
                self.account_creation()
            elif menu_1 == '2':
                self.account_login()

    def exit(self):
        self.conn.close()
        print("\nBye!")
        self.sys.exit()


my_bank = Banking()
my_bank.main_menu()
