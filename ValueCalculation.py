import numpy as np


class ValueCalculation:

    def __init__(self, players, nashs):

        self.player1 = players[0]

        self.nashs = nashs

    def calculateValue(self):

        matrix = np.copy(self.player1.gain)

        matrix = matrix.transpose()

        # on reecupere la 1ere colonne de la matrice
        row = matrix[0]

        # on reecupere le 1er profil du 1er equilibre de nash
        nash = list(self.nashs[0][0])

        return np.dot(row, nash)
