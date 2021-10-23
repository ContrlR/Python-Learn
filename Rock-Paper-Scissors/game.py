

class RPS:

    def __init__(self):

        self.roshambo = ('rock', 'paper', 'scissors')
        self.score_board = dict()

    def fill_scores(self):
        file = open('rating.txt', 'r', encoding='utf-8')
        file_read = file.readlines()
        for line in file_read:
            line_as_list = line.split()
            self.score_board[line_as_list[0]] = int(line_as_list[1])
        file.close()

    def exit_game(self):
        print('Bye!')
        file = open('rating.txt', 'w')
        scores = str(self.score_board)
        scores = scores.replace('}', '')
        scores = scores.replace('{', '')
        scores = scores.replace("'", '')
        scores = scores.replace(':', '')
        scores = scores.replace(', ', '\n')
        file.write(scores)
        file.close()

    def mechanics(self, user, pc, name):

        winner = False

        if pc == user:
            print(f'There is a draw ({pc})')
            self.score_board[name] += 50
        else:
            if pc == 'rock':
                if user in ('paper', 'air', 'water', 'dragon', 'devil', 'lighting', 'gun'):
                    winner = True
            elif pc == 'fire':
                if user in ('rock', 'air', 'water', 'dragon', 'devil', 'lighting', 'gun'):
                    winner = True
            elif pc == 'scissors':
                if user in ('rock', 'fire', 'water', 'dragon', 'devil', 'lighting', 'gun'):
                    winner = True
            elif pc == 'snake':
                if user in ('rock', 'fire', 'scissors', 'dragon', 'devil', 'lighting', 'gun'):
                    winner = True
            elif pc == 'human':
                if user in ('rock', 'fire', 'scissors', 'snake', 'devil', 'lighting', 'gun'):
                    winner = True
            elif pc == 'tree':
                if user in ('rock', 'fire', 'scissors', 'snake', 'human', 'lighting', 'gun'):
                    winner = True
            elif pc == 'wolf':
                if user in ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'gun'):
                    winner = True
            elif pc == 'sponge':    ####
                if user in ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'):
                    winner = True
            elif pc == 'paper':
                if user in ('sponge', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'):
                    winner = True
            elif pc == 'air':
                if user in ('sponge', 'paper', 'scissors', 'snake', 'human', 'tree', 'wolf'):
                    winner = True
            elif pc == 'water':
                if user in ('sponge', 'paper', 'air', 'snake', 'human', 'tree', 'wolf'):
                    winner = True
            elif pc == 'dragon':
                if user in ('sponge', 'paper', 'air', 'water', 'human', 'tree', 'wolf'):
                    winner = True
            elif pc == 'devil':
                if user in ('sponge', 'paper', 'air', 'water', 'dragon', 'tree', 'wolf'):
                    winner = True
            elif pc == 'lighting':
                if user in ('sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'wolf'):
                    winner = True
            elif pc == 'gun':
                if user in ('sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lighting'):
                    winner = True

            if winner:
                print(f'Well done. Computer chose {pc} and failed')
                self.score_board[name] += 100

            else:
                print(f'Sorry, but computer chose {pc}')

    def game(self):
        from random import choice

        self.fill_scores()

        name = input('Enter your name: ')
        print(f'Hello, {name}')
        if name not in self.score_board:
            self.score_board[name] = 0

        game_mode = input('''Type which options to include. Use commas! Options are:
        rock,gun,lightning,devil,dragon,water,air,
        paper,sponge,wolf,tree,human,snake,scissors,fire
''')
        if game_mode == '':
            pass    # roshambo  is already preset  R P S  if left Blank
        else:
            game_mode = game_mode.split(sep=',')
            self.roshambo = game_mode
        print(f'Okay, the computer will chose from: {self.roshambo}')

        print('!rating to check your score')
        print('!exit to save your score and leave the game.')
        print('!leader to check the leader board.')
        print('Okay, let\'s start!!')
        while True:

            pc = choice(self.roshambo)
            user = input()

            if user in self.roshambo:
                self.mechanics(user, pc, name)

            elif user == '!exit':
                self.exit_game()
                break
            elif user == '!rating':
                print(self.score_board[name])
            elif user == '!leader':
                for key in self.score_board:
                    print(key, ':', self.score_board[key])
            elif user not in self.roshambo:
                print('Invalid input')


my_game = RPS()
my_game.game()
