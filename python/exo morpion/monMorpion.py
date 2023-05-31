# import random


class Morpion:

    """
    Le constructeur de la classe Morpion est définis par __init__
    self = objet cible permettant d'acceder aux attributs/fonctionnalités
    """
    def __init__(self):
        self.grid = []

# construction de la grille : 
    def create_grid(self):
        for i in range(3):
            print("_ " * 3)


# Initialisation du jeux
    def start_game(self):
        self.create_grid()
        player = "x"


# change le tour du joueur
    def switch_turn(self, player):
        return "o" if player == "x" else "x"


# vérifie la grille
    def win_verify(self, player):
        win = False


        



Morpion().start_game()