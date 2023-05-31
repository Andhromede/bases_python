import random


class Morpion:

    """
    Le constructeur de la classe Morpion est définis par __init__
    self = objet cible permettant d'acceder aux attributs/fonctionnalités
    """
    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.grid.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.grid[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.grid)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.grid[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.grid[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.grid[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.grid[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.grid:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_grid_filled(self):
        for row in self.grid:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_grid()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_grid()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_grid_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of grid
        print()
        self.show_grid()


# starting the game
Morpion().start()