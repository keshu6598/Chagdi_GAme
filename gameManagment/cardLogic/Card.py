"""
This module contains programmatic representation of playing
cards and their suits information
"""
import gameManagment.enums.cardConstants as cardConstants
import gameManagment.enums.gameError as gError
import random


class Card:
    def __init__(self,
                 card_value,
                 card_suit):
        """
        @value: Define's the rank of the card.
        @suit: Define's the suit of the card.
        """
        if card_value not in cardConstants.VALID_RANKS:
            raise gError.InvalidRank
        if card_suit not in cardConstants.VALID_SUITS:
            raise gError.InvalidSuit

        self.value = card_value
        self.suit  = card_suit

    def cardGameValue(self, suits_weight):
        """
        This method determine the value of cards with
        will be require to determine who is wining
        the current round.
        """
        return suits_weight[self.suit - 1] * self.value

    def cardActualValue(self):
        """
        This method is used to determine the current
        score of which will be
        for ex Q<hearts> .. = 50.
        """
        return cardConstants.cardScore[self.value]


def generateRandom52cards():
    """
    Generate list of 52 cards in random order.
    """
    all52Cards = []
    for card_value in cardConstants.VALID_RANKS:
        for card_suit in cardConstants.VALID_SUITS:
            all52Cards.append(Card(card_value, card_suit))

    random.shuffle(all52Cards)
    random.shuffle(all52Cards)
