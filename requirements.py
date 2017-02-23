class Requirement(object):
    '''
    Base requirement, takes a game state function
    '''
    def __init__(self, requirement_function, requirement_data):
        self.requirement_function = requirement_function
        self.requirement_data = requirement_data

    def requirement_met(self):
        return self.requirement_function(self.requirement_data)

class Tap(object):
    '''
    I'd prefer this be called TapCard, in the same verb->noun form as other functions
    '''

    def __init__(self, game_state, card):
        super(self, Tap).__init__(game_state.untapped, card)


class PayMana(object):
    def __init__(self, c_dict):
        self.c_dict = c_dict

    def requirement_met(self, game_state):
        return game_state.mana_floating(self.c_dict)


class ExileCard(object):
    def __init__(self, card_to_exile):
        self.card_to_exile = card_to_exile

    def requirement_met(self, game_state):
        return game_state.card_in_hand(self.card_to_exile)


class InHand(object):
    def __init__(self, card_in_hand):
        self.card_in_hand = card_in_hand

    def requirement_met(self, game_state):
        return game_state.card_in_hand(self.card_in_hand)


class InPlay(object):
    def __init__(self, card_in_play):
        self.card_in_play = card_in_play

    def requirement_met(self, game_state):
        return game_state.card_in_play(self.card_in_play)


class Untapped(object):
    def __init__(self, card):
        self.card = card

    def requirement_met(self, game_state):
        return game_state.untapped(self.card)
