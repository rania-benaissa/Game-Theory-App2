
from SupportEnumAlgo import SupportEnumAlgo

from ValueCalculation import ValueCalculation


class Game():

    def __init__(self, players):

        self.players = players

    def supportEnumAlgo(self):

        sea = SupportEnumAlgo(self.players)
        return sea.supportEnumAlgo()

    def calculateValue(self, nashs):
        va = ValueCalculation(self.players, nashs)
        return va.calculateValue()
