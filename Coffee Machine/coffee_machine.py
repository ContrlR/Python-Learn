#! env\bin\python
# Ryan Simmons
# Coffee Machine Project


class CoffeeMachine:

    # the values in supplies refers to 1-1  with this
    supply_str = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']

    def __init__(self, supplies):

        self.supplies = supplies

    def supply_checker(self, drink):

        # Money is represented as the value taken (negative) there always less than and should not cause an error
        for i in range(len(drink)):
            if drink[i] > self.supplies[i]:
                print(f'Sorry not enough {self.supply_str[i]} !')
                break
        else:
            for i in range(len(drink)):
                self.supplies[i] -= drink[i]    # Completes the transaction for the drink
            print('I have enough resources, making you a coffee!')

    def drink_maker(self):

        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

        #  Inputs the value for particular drinks into supply_checker()
        if drink == '1':
            espresso = [250, 0, 16, 1, -4]
            self.supply_checker(espresso)

        elif drink == '2':
            latte = [350, 75, 20, 1, -7]
            self.supply_checker(latte)

        elif drink == '3':
            cappuccino = [200, 100, 12, 1, -6]
            self.supply_checker(cappuccino)

        else:
            return

    def filler(self):

        #  supply_str = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']

        self.supplies[0] += int(input(f'Write how many ml of {self.supply_str[0]} do you want to add: '))
        self.supplies[1] += int(input(f'Write how many ml of {self.supply_str[1]} do you want to add: '))
        self.supplies[2] += int(input(f'Write how many grams of {self.supply_str[2]} do you want to add: '))
        self.supplies[3] += int(input(f'Write how many {self.supply_str[3]} of coffee do you want to add: '))

    def remaining(self):

        #  supply_str = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']

        print('The coffee machine has:')
        for i in range(len(self.supplies)):
            print(f'{self.supplies[i]} of {self.supply_str[i]}')

    # Only method that user should have to interact with, Like a real cafe!
    def barista(self):

        while True:

            action = input('Write action (buy, fill, take, remaining, exit): ')

            if action == 'buy':
                self.drink_maker()
            elif action == 'fill':
                self.filler()
            elif action == 'take':
                print(f'I gave you ${self.supplies[4]}')
                self.supplies[4] = 0
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                break

            print()


# Debugging
my_supplies = [400, 540, 120, 9, 550]
my_coffee = CoffeeMachine(my_supplies)
my_coffee.barista()
