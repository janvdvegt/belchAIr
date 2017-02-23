from color_dict import ColorDict
from config import ZONES
from action import Action
from consequences import UntapPermanents, StormCountZero, DealGoblinDamage, DrawCard
import cards
from numpy.random import choice
from random import shuffle


class GameState(object):
    def __init__(self):
        self.deck = {}
        self.hand = {}
        self.exile = {}
        self.sideboard = {}
        self.battlefield = {}
        self.graveyard = {}
        self.tapped = {}

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
            self.graveyard[card.name] = 0
            if card.is_tappable():
                self.tapped[card.name] = 0
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

    def storm_count_zero(self):
        self.storm_count = 0

    def goblin_damage(self):
        self.opp_life_total -= self.goblins

    def damage_opponent(self, damage):
        self.opp_life_total -= damage

    def untap_permanents(self):
        for card, _, _ in self.cards:
            if card.is_tappable():
                self.tapped[card.name] = 0

    def add_rite_mana(self):
        self.add_mana(ColorDict({'Red': 2 + self.graveyard['Rite of Flame']}))

    def belch(self):
        deck_list = self._list_deck(True, True)
        total_damage = 0
        for card in deck_list:
            if card == 'Taiga':
                total_damage *= 2
                break
            total_damage += 1
        self.damage_opponent(total_damage)

    def discard_hand(self):
        for card_name in self.hand:
            self.graveyard[card_name] += self.hand[card_name]
            self.hand[card_name] = 0

    def shuffle(self):
        self.taiga_bottom = False

    def draw_cards(self, amount):
        cards_to_draw = choice(self._list_deck(), amount, False)
        for card_to_draw in cards_to_draw:
            self.deck[card_to_draw] -= 1
            self.hand[card_to_draw] += 1

    def _list_deck(self, include_Taiga=True, shuffle_list=False):
        deck_list = []
        for card_name in self.deck:
            if card_name != 'Taiga' or not self.taiga_bottom:
                deck_list.extend([card_name for _ in range(self.deck[card_name])])
        if shuffle_list:
            shuffle(deck_list)
        if self.taiga_bottom and include_Taiga:
            deck_list.append('Taiga')
        return deck_list

    def tap_card(self, card):
        self.tapped[card.name] += 1

    def add_storm(self):
        self.storm_count += 1

    def add_goblins(self):
        self.goblins += 2 * self.storm_count

    def add_mana(self, c_dict):
        self.mana_pool.add_mana(c_dict)

    def reduce_mana(self, c_dict):
        self.mana_pool.subtract_mana(c_dict)

    def increase_card_count(self, card, zone):
        self._zone_dispatcher(zone)[card.name] += 1

    def reduce_card_count(self, card, zone):
        self._zone_dispatcher(zone)[card.name] -= 1

    def _zone_dispatcher(self, zone):
        if zone == 'Graveyard':
            return self.graveyard
        elif zone == 'Hand':
            return self.hand
        elif zone == 'Exile':
            return self.exile
        elif zone == 'Deck':
            return self.deck
        elif zone == 'Sideboard':
            return self.sideboard
        raise ValueError('Incorrect zone type', zone)