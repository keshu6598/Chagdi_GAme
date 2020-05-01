"""
This file contains all the constants that will be require to
manage various cards.
"""

# Various constants to represent current suits.
# When no Suit is assigned.
NOT_VALID_SUIT_ASSIGNED = 0

# Some valid suits.
HEARTS   = 1
SPADES   = 2
DIAMONDS = 3
CLUBS    = 4

# List of all valid suits
VALID_SUITS = [HEARTS, SPADES, DIAMONDS, CLUBS]

# All card ranks.
NO_RANK = 0
TWO     = 2
THREE   = 3
FOUR    = 4
FIVE    = 5
SIX     = 6
SEVEN   = 7
EIGHT   = 8
NINE    = 9
TEN     = 10
JACK    = 11
QUEEN   = 12
KING    = 13
ACE     = 14

# List of all valid ranks.
VALID_RANKS = [THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]

cardScore = {
    THREE: 3,
    FOUR:  4,
    FIVE:  5,
    SIX:   6,
    SEVEN: 7,
    EIGHT: 8,
    NINE:  9,
    TEN:   10,
    JACK:  11,
    QUEEN: 50,
    KING:  12,
    ACE:   1
}