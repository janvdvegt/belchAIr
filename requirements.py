class Requirement(object):
    """
    Base requirement, takes a game state function
    """
    def __init__(self):
        raise NotImplementedError()

    def requirement_met(self):
        raise NotImplementedError()


class CardUntapped(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.untapped(self.card)


class ManaInPool(Requirement):
    def __init__(self, c_dict):
        self.c_dict = c_dict

    def requirement_met(self, game_state):
        return game_state.mana_floating(self.c_dict)


class CardInHand(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.card_in_hand(self.card)


class CardNotInHand(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return not game_state.card_in_hand(self.card)


class CardInPlay(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.card_in_play(self.card)


class CardInSideboard(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.card_in_sideboard(self.card)


class CardInDeck(Requirement):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.card_in_deck(self.card)
