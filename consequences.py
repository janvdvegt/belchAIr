class Consequence(object):
    """
    Base Consequence class, which is used for Action constructors.
    """
    #def __init__(self):
    #    pass

    def happen(self, game_state):
        pass


class ManaConsequence(Consequence):
    """
    For Consequences that affect mana
    """
    def __init__(self, c_dict):
        self.c_dict = c_dict


class CardConsequence(Consequence):
    """
    Consequences for cards
    """
    def __init__(self, card):
        self.card = card


class ReduceMana(ManaConsequence):
    """
    Pay Mana
    """
    def happen(self, game_state):
        game_state.reduce_mana(self.c_dict)


class AddMana(ManaConsequence):
    """
    Gain Mana
    """
    def happen(self, game_state):
        game_state.add_mana(self.c_dict)


class MoveCard(CardConsequence):
    """
    Moving a Card
    """
    def __init__(self, card, from_zone, to_zone):
        super(self, MoveCard).__init__(card)
        self.from_zone = from_zone
        self.to_zone = to_zone

    def happen(self, game_state):
        game_state.reduce_card_count(self.card, self.from_zone)
        game_state.increase_card_count(self.card, self.to_zone)


class Tap(CardConsequence):
    """
    Tapping a Card
    """
    def happen(self, game_state):
        game_state.tap_card(self.card)


class AddStorm(Consequence):
    def happen(self, game_state):
        game_state.add_storm()


class AddGoblins(Consequence):
    def happen(self, game_state):
        game_state.add_goblins()


class DrawCard(Consequence):
    def __init__(self, amount=1):
        self.amount = amount

    def happen(self, game_state):
        game_state.draw_cards(self.amount)


class Shuffle(Consequence):
    def happen(self, game_state):
        game_state.shuffle()


class DiscardHand(Consequence):
    def happen(self, game_state):
        game_state.discard_hand()


class Belch(Consequence):
    def happen(self, game_state):
        game_state.belch()


class AddRiteMana(Consequence):
    def happen(self, game_state):
        game_state.add_rite_mana()


class UntapPermanents(Consequence):
    def happen(self, game_state):
        game_state.untap_permanents()


class DealGoblinDamage(Consequence):
    def happen(self, game_state):
        game_state.goblin_damage()


class StormCountZero(Consequence):
    def happen(self, game_state):
        game_state.storm_count_zero()
