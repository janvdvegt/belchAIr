# All of the constructors are the same. Move to base class.
class Requirement(object):
    """
    Base Requirement
    """
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        raise NotImplementedError

    def __str__(self):
        return str(type(self))


class CardUntapped(Requirement):
    """
    The Card must be untapped.
    """

    def requirement_met(self, game_state):
        return game_state.untapped(self.card)


class ManaInPool(Requirement):
    # This should accept a card IMHO. Why is this mana in the pool? Why is this not a function of the game state?
    # I think this should be a consequence of something else.
    # If anything a card should know how to represent it's own mana requirements.
    # I implemented CheckForManaAvailable as a consequence.
    """
    A ColorDict of mana must be floating in the mana pool.
    """
    def __init__(self, c_dict):
        self.c_dict = c_dict

    def requirement_met(self, game_state):
        return game_state.mana_floating(self.c_dict)


class CardInHand(Requirement):
    """
    A Card must be in the Hand.
    """

    def requirement_met(self, game_state):
        return game_state.card_in_hand(self.card)


class CardNotInHand(Requirement):
    """
    A Card must not be in the Hand.
    """

    def requirement_met(self, game_state):
        return not game_state.card_in_hand(self.card)


class CardInPlay(Requirement):
    """
    A Card must be on the Battlefield.
    """

    def requirement_met(self, game_state):
        return game_state.card_in_play(self.card)


class CardInSideboard(Requirement):
    """
    A Card must be in the Sideboard.
    """

    def requirement_met(self, game_state):
        return game_state.card_in_sideboard(self.card)


class CardInDeck(Requirement):
    """
    A Card must be in the Deck.
    """

    def requirement_met(self, game_state):
        return game_state.card_in_deck(self.card)
