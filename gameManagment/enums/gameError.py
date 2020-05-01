"""
This file contains list of all the custom error
that may be require to be throw during special cases.
"""


class AllPlayersJoinedTheGame(Exception):
    """
    This Exception is there to make game know
    that all the player had joined the game
    no more player can join the game.
    """
    pass


class InvalidRank(Exception):
    """
    This Exception is raised to make indicate
    that invalid card rank had been substituted.
    """
    pass


class InvalidSuit(Exception):
    """
    This Exception is raised to make indicate
    that invalid card suit had been substituted.
    """
    pass
