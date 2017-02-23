class Consequence(object):
    def __init__(self):
        pass


class ReduceMana(Consequence):
    def __init__(self, c_dict):
        self.c_dict = c_dict

    def happen(self, game_state):
        game_state.reduce_mana(self.c_dict)


class AddMana(Consequence):
    def __init__(self, c_dict):
        self.c_dict = c_dict

    def happen(self, game_state):
        game_state.add_mana(self.c_dict)


class MoveCard(Consequence):
    def __init__(self, card, from_zone, to_zone):
        self.card = card
        self.from_zone = from_zone
        self.to_zone = to_zone

    def happen(self, game_state):
        game_state.reduce_card_count(self.card, self.from_zone)
        game_state.increase_card_count(self.card, self.to_zone)


class Tap(Consequence):
    def __init__(self, card):
        self.card = card

    def happen(self, game_state):
        game_state.tap_card(self.card)


class AddStorm(Consequence):
    def happen(self, game_state):
        game_state.add_storm()
