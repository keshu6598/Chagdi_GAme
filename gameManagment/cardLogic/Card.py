"""
This module contains programmatic representation of playing
cards and their suits information
"""


class Card:
    def __init__(self,
                 card_value,
                 card_suit):
        self.value = card_value
        self.suit  = card_suit

    def cardGameValue(self, suitsWeight):
        """
        This method determine the value of cards with
        will be require to determine who is wining
        the current round.
        """
        pass

    def cardActualValue(self):
        """
        This method is used to determine the current
        score of which will be
        for ex Q<hearts> .. = 50.
        """
        pass


def generateRandom52cards():
    """
    Generate list of 52 cards in random order.
    """
    pass
