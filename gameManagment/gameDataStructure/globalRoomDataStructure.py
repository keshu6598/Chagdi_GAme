"""
This Module contains data-structures and functions that will be
require to manage the global variable for the given gameState.
"""
from gameManagment.cardLogic.Card import generateRandom52cards

import gameManagment.enums.stateConstants as stateConstant
import gameManagment.enums.cardConstants  as cardsConstant


class GlobalRoomDataStructure:
    def __init__(self):
        """
        #TODO(Abhishek) Write definition of all variables.
        """
        self.allConnectedPlayers = []
        self.cardRemainingToDistribute = generateRandom52cards()
        self.cardThrowingStartAt = stateConstant.NO_FIXED_STARTING_PLAYER
        self.currentGameState = stateConstant.STATE_SET_TO_CARD_DISTRIBUTION
        self.highestBid = 0
        self.isBidOver = False
        self.mainPlayer = stateConstant.MAIN_PLAYER_IS_NOT_ASSIGNED
        self.maximumCardForGivenRound = 0
        self.playerAvailableForBid = [0, 1, 2, 3, 4, 5]
        self.roundWiningPlayerID = stateConstant.NO_FIXED_STARTING_PLAYER
        self.suitWeight = [0, 0, 0, 0]
        self.teamDistribution = [stateConstant.NO_TEAM_ASSIGNED] * 6
        self.trumpSet = cardsConstant.NOT_ASSIGNED

    def joinNewPlayer(self, player_name):
        """
        This method allows addition of new player.
        """
        pass

    def startNewRoundWith(self, suit_name):
        """
        This method update various weight of suits as
        soon as new round of game start
        """
        pass

    def setTrump(self, suit_name):
        """
        This method update trump name and various weight
        of suits as soon as trump is set.
        """
        pass

    def endCurrentRound(self):
        """
        This method update weight of various suits as
        soon as current round is over.
        """
        pass

    def getWiningPlayerID(self,
                          player_id,
                          card_used_by_player):
        """
        This method determine stepwise step which player is wining
        the current round for game.

        Problem with determining the winner of game by collecting
        all 6 card is that we can set trump in the middle of game
        which updates the weight of the suits and its is kind of
        unnatural to determine. In real game also we determine
        who is winning game step wise step rather than determining
        it at onces.
        """
        pass
