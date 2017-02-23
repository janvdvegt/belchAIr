from color_dict import ColorDict
from config import ZONES
from action import Action
from consequences import UntapPermanents, StormCountZero, DealGoblinDamage, DrawCard
import cards


class GameState(object):
    def __init__(self):
        self.deck = {}
        self.hand = {}
        self.exile = {}
        self.sideboard = {}
        self.battlefield = {}

        self.mana_pool = ColorDict()
        self.goblins = 0
        self.storm_count = 0
        self.opp_life_total = 20
        self.taiga_bottom = False

        self.cards = []

    def add_card(self, card, maindeck, sideboard):
        self.cards.append((card, maindeck, sideboard))

    def reset_game(self):
        for card, maindeck, sideboard in self.cards:
            self.deck[card.name] = maindeck
            self.sideboard[card.name] = sideboard
            self.hand[card.name] = 0
            self.exile[card.name] = 0
            self.battlefield[card.name] = 0
        self.mana_pool = ColorDict()
        self.goblins = 0
        self.storm_count = 0
        self.opp_life_total = 20
        self.taiga_bottom = False

    def possible_actions(self):
        """
        List of binary numbers to represent if that action is available

        :return:
        """
        pass

    def all_actions(self):
        actions = []
        actions.append(Action(requirements=[], consequences=[UntapPermanents(),
                                                             StormCountZero(),
                                                             DealGoblinDamage(),
                                                             DrawCard()]))
        for card in self.cards:
            actions.extend(card.actions)
            print(card.name, len(card.actions))
        print(len(actions))


    def state_space(self):
        pass

print(seething_song.name)