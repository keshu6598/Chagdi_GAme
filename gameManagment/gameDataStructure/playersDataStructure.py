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
        #TODO(Abhishek) Write definition of all variables.
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
        pass

    def canPlayerBid(self, new_bid):
        """
        Determine can player have new bid.
        """
        pass

    def useCard(self, card_info):
        """
        This method check whether player can use particular
        card it soo it remove's that particular car from
        pack of his card and return's True.
        """
        pass

    def to_be_deleted(self, card_info):
        print(card_info);
