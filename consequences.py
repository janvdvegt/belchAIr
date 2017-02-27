class Consequence(object):
    """
    Base Consequence class, which is used for Action constructors.
    """
    def __str__(self):
        return str(type(self))


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
    def resolve(self, game_state):
        game_state.reduce_mana(self.c_dict)

    def __str__(self):
        return 'Reduce mana with: ' + str(self.c_dict)

class CheckForManaAvailable(ManaConsequence):
    """
    Check for Mana in Pool
    """

    def resolve(self, game_state):
        return game_state.mana_floating(self.c_dict)

class AddMana(ManaConsequence):
    """
    Gain Mana
    """
    def resolve(self, game_state):
        game_state.add_mana(self.c_dict)

    def __str__(self):
        return 'Increase mana with: ' + str(self.c_dict)


class MoveCard(CardConsequence):
    """
    Moving a Card
    """
    def __init__(self, card, from_zone, to_zone):
        super(MoveCard, self).__init__(card)
        self.from_zone = from_zone
        self.to_zone = to_zone

    def resolve(self, game_state):
        game_state.reduce_card_count(self.card, self.from_zone)
        game_state.increase_card_count(self.card, self.to_zone)

    def __str__(self):
        return 'Move ' + self.card + ' from: ' + str(self.from_zone) + ' to: ' + self.to_zone


class Tap(CardConsequence):
    """
    Tap a Card.
    """
    def resolve(self, game_state):
        game_state.tap_card(self.card)

    def __str__(self):
        return 'Tapping ' + self.card


class AddStorm(Consequence):
    """
    Add a Storm Counter.
    """
    def resolve(self, game_state):
        game_state.add_storm()

    def __str__(self):
        return 'Adding storm'

class AddGoblins(Consequence):
    """
    Add a Goblin to the Battlefield.
    """
    def resolve(self, game_state):
        game_state.add_goblins()

    def __str__(self):
        return 'Making goblins'

class DrawCard(Consequence):
    """
    Draw a Card from the Deck.
    """
    def __init__(self, amount=1):
        self.amount = amount

    def resolve(self, game_state):
        game_state.draw_cards(self.amount)
        return game_state.reward()

    def __str__(self):
        return 'Drawing ' + str(self.amount) + ' cards'


class Shuffle(Consequence):
    """
    Shuffle the Deck.
    """
    def resolve(self, game_state):
        game_state.shuffle()

    def __str__(self):
        return 'Shuffle'

class DiscardHand(Consequence):
    """
    Discard the Hand.
    """
    def resolve(self, game_state):
        game_state.discard_hand()

    def __str__(self):
        return 'Discarding hand'

class Belch(Consequence):
    """
    Activate Goblin Charbelcher.
    """
    def resolve(self, game_state):
        game_state.belch()
        print(self)
        return game_state.reward()

    def __str__(self):
        return 'BURRRRRRPPppppp'

class AddRiteMana(Consequence):
    """
    Add Mana from Rite of Flame
    """
    def resolve(self, game_state):
        game_state.add_rite_mana()

    def __str__(self):
        return 'Adding Rite of Flame mana'

class UntapPermanents(Consequence):
    def resolve(self, game_state):
        game_state.untap_permanents()

    def __str__(self):
        return 'Untap all permanents'


class DealGoblinDamage(Consequence):
    def resolve(self, game_state):
        game_state.goblin_damage()
        return game_state.reward()

    def __str__(self):
        return 'Attack with all goblins'


class StormCountZero(Consequence):
    def resolve(self, game_state):
        game_state.storm_count_zero()

    def __str__(self):
        return 'Storm count back to zero'

class ResetManaPool(Consequence):
    def resolve(self, game_state):
        game_state.reset_mana_pool()

    def __str__(self):
        return 'Reset mana pool'

class AddTurn(Consequence):
    # I think there should be some more meta consequences and requirements like this
    # A ClearStack Consequence for example, with an EmptyStack requirement 
    # The EmpytStack requirement would indicate sorcery speed effects. 
    def resolve(self, game_state):
        game_state.add_turn()

    def __str__(self):
        return 'Adding turn'
