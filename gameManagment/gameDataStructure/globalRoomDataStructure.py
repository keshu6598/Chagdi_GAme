"""
This Module contains data-structures and functions that will be
require to manage the global variable for the given gameState.
"""
from gameManagment.cardLogic.Card import generateRandom52cards
from gameManagment.gameDataStructure.playersDataStructure import PlayersData

import gameManagment.enums.stateConstants as stateConstant
import gameManagment.enums.cardConstants  as cardsConstant
import gameManagment.enums.gameError as gError


class GlobalRoomDataStructure:
    def __init__(self):
        """
        @allConnectedPlayer: This variable is list of all the player
                             Which are connected for a given game.
        @cardRemainingToDistribute: This is the list of randomly shuffled
                                    card which we have to distribute as soon
                                    as new player join the game.
        @playerThrowingStartAt: ID of the player from where game will start.
        @currentGameState: State variable defining the state of given game.
        @highestBid: Define highest bid for a given game, ones the biding
                     period is over this can not be changed.
        @mainPlayer: Define the name of the main player for the given
                     game.
        @maximumCardForGivenRound: Defines the maximum value for the given
                                   round.
        @playerAvailableForBid: List of all the player who can bid currently.
        @roundWiningPlayerID: ID of player who is currently winning the round.
        @suitWeight: Weight of given suits use to which car has the maximum value.
        @teamDistribution: Define the teams in which various player is present.
        @trumpSet: The value of trump that had been set.
        @canShowTrump: Define whether we can show the trump to all user.
        @currentRoundTotal: Define's the current total for the given round.
        """
        self.allConnectedPlayers = []
        self.cardRemainingToDistribute = generateRandom52cards()
        self.playerThrowingStartAt = stateConstant.NO_FIXED_STARTING_PLAYER
        self.currentGameState = stateConstant.STATE_SET_TO_CARD_DISTRIBUTION
        self.highestBid = 0
        self.mainPlayer = stateConstant.MAIN_PLAYER_IS_NOT_ASSIGNED
        self.maximumCardForGivenRound = 0
        self.playerAvailableForBid = [0, 1, 2, 3, 4, 5]
        self.roundWiningPlayerID = stateConstant.NO_FIXED_STARTING_PLAYER
        self.suitWeight = [0, 0, 0, 0]
        self.teamDistribution = [stateConstant.NO_TEAM_ASSIGNED] * 6
        self.trumpSet = cardsConstant.NOT_VALID_SUIT_ASSIGNED
        self.canShowTrump = False
        self.currentRoundTotal = 0

    def joinNewPlayer(self, player_name):
        """
        This method allows addition of new player.
        """
        if len(self.allConnectedPlayers) >= 6:
            return gError.AllPlayersJoinedTheGame

        new_player = PlayersData(len(self.allConnectedPlayers), player_name)
        new_player.assignAllCardsToPlayer(self.cardRemainingToDistribute[-13:])
        self.cardRemainingToDistribute = self.cardRemainingToDistribute[:-13]
        return None

    def startNewRoundWith(self, suit_name):
        """
        This method update various weight of suits as
        soon as new round of game start
        """
        self.suitWeight[suit_name - 1] = 1

    def showTrump(self, suit_name):
        """
        This method update trump name and various weight
        of suits as soon as trump is set.
        """
        self.suitWeight[suit_name - 1] = 50
        self.canShowTrump = True

    def endCurrentRound(self):
        """
        This method update weight of various suits as
        soon as current round is over.
        """
        for idx, val in enumerate(self.suitWeight):
            if val % 1 == 1:
                self.suitWeight[idx] = self.suitWeight[idx] - 1
                break
        self.maximumCardForGivenRound = 0
        self.roundWiningPlayerID = stateConstant.NO_FIXED_STARTING_PLAYER
        self.currentRoundTotal = 0

    def getWiningPlayerIDAndTotal(self,
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
        it at ones.
        """
        if card_used_by_player.cardGameValue(self.suitWeight) > self.maximumCardForGivenRound:
            self.maximumCardForGivenRound = card_used_by_player.cardGameValue(self.suitWeight)
            self.roundWiningPlayerID = player_id
        self.currentRoundTotal = self.currentRoundTotal + card_used_by_player.cardActualValue()
        return self.roundWiningPlayerID, self.currentRoundTotal
