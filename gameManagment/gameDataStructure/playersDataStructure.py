"""
This module contains various data-structures and functions that
will be require to manage the data corresponding to each player.
"""
import gameManagment.enums.stateConstants as stateConstant


class PlayersData:
    def __init__(self,
                 player_id,
                 player_name):
        """
        @playerID: ID for the given player.
        @playerName: Name of the player.
        @playerCards: List of all the cards available to
                      the player.
        @isPlayerAvailableForBid: This variable show that current
                                  player can bid or not.
        @isStarPlayer: This shows whether this player is player
                       for the given game.
        @playerTeam: Defines the team of the player.
        @playerScore: Defines the total score accumulated by the player.
        """
        self.playerID = player_id
        self.playerName = player_name
        self.playerCards = []
        self.isPlayerAvailableForBid = True
        self.currentPlayerMaxBid = 0
        self.isStarPlayer = False
        self.playerTeam = stateConstant.NO_TEAM_ASSIGNED
        self.playerScore = 0

    def assignAllCardsToPlayer(self, card_distribution):
        """
        Provide card distribution to given player
        """
        self.playerCards = card_distribution

    def canPlayerBid(self, new_bid):
        """
        Determine can player have new bid.
        """
        if self.isPlayerAvailableForBid is True and new_bid > self.currentPlayerMaxBid:
            return True
        return False

    def useCard(self, card_info):
        """
        This method check whether player can use particular
        card it soo it remove's that particular car from
        pack of his card and return's True.
        """
        if card_info in self.playerCards:
            self.playerCards.remove(card_info)
            return True
        return False

    def updatePlayerTotal(self, new_total):
        """
        This method update's the current total for
        the given player.
        """
        self.playerScore = self.playerScore + new_total
