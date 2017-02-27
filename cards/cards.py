from mana_iterator import color_combinations, fill_up_remaining_colors
from requirements import ManaInPool, CardInHand, CardUntapped, CardInPlay, CardInSideboard, \
                         CardInDeck, CardNotInHand
from consequences import AddMana, MoveCard, Tap, AddStorm, AddRiteMana, AddGoblins, DrawCard, \
                         Shuffle, DiscardHand, Belch, ReduceMana
from color_dict import ColorDict
from action import Action
from card import Card
from config import COLORS, CARDS_FOR_CHROME_MOX, CARDS_FOR_BURNING_WISH


class SeethingSong(Card):
    def __init__(self):
        super(SeethingSong, self).__init__('Seething Song')
        seething_song_action = Action('Seething Song',
                                      'Play',
                                      requirements=[CardInHand(self.name)],
                                      consequences=[AddMana(ColorDict({'Red': 5})),
                                                    MoveCard(self.name, 'Hand', 'Graveyard'),
                                                    AddStorm()])
        self.add_mana_action(seething_song_action,
                             paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 2})))

class Taiga(Card):
    def __init__(self):
        super(Taiga, self).__init__('Taiga', is_tappable=True, is_permanent=True)
        taiga_action_play = Action('Taiga',
                                   'Play',
                                   requirements=[CardInHand(self.name)],
                                   consequences=[MoveCard(self.name, 'Hand', 'Battlefield')])
        taiga_action_tap = Action('Taiga',
                                  'Tap',
                                  requirements=[CardUntapped(self.name)],
                                  consequences=[Tap(self.name)])
        self.add_action(taiga_action_play)
        self.add_mana_action(
            taiga_action_tap,
            adding=fill_up_remaining_colors(1, ['Red', 'Green'], ColorDict(), []))


class ElvishSpiritGuide(Card):
    def __init__(self):
        super(ElvishSpiritGuide, self).__init__('Elvish Spirit Guide')
        elvish_spirit_guide_action = Action('Elvish Spirit Guide',
                                            'Exile',
                                            requirements=[CardInHand(self.name)],
                                            consequences=[AddMana(ColorDict({'Green': 1})),
                                                          MoveCard(self.name, 'Hand', 'Exile')])

        self.add_action(elvish_spirit_guide_action)


class SimianSpiritGuide(Card):
    def __init__(self):
        super(SimianSpiritGuide, self).__init__('Simian Spirit Guide')
        simian_spirit_guide_action = Action('Simian Spirit Guide',
                                            'Exile',
                                            requirements=[CardInHand(self.name)],
                                            consequences=[AddMana(ColorDict({'Red': 1})),
                                                          MoveCard(self.name, 'Hand', 'Exile')])
        self.add_action(simian_spirit_guide_action)

class TinderWall(Card):
    def __init__(self):
        super(TinderWall, self).__init__('Tinder Wall', is_permanent=True)
        tinder_wall_play_action = Action('Tinder Wall',
                                         'Play',
                                         requirements=[CardInHand(self.name),
                                                       ManaInPool(ColorDict({'Green': 1}))],
                                         consequences=[MoveCard(self.name, 'Hand', 'Battlefield'),
                                                       ReduceMana(ColorDict({'Green': 1})),
                                                       AddStorm()])
        tinder_wall_mana_action = Action('Tinder Wall',
                                         'Sacrifice',
                                         requirements=[CardInPlay(self.name)],
                                         consequences=[MoveCard(self.name, 'Battlefield', 'Graveyard'),
                                                       AddMana(ColorDict({'Red': 2}))])
        self.add_action(tinder_wall_play_action)
        self.add_action(tinder_wall_mana_action)

class PyreticRitual(Card):
    def __init__(self):
        super(PyreticRitual, self).__init__('Pyretic Ritual')
        pyretic_ritual_action = Action('Pyretic Ritual',
                                       'Play',
                                       requirements=[CardInHand(self.name)],
                                       consequences=[AddMana({'Red': 3}),
                                                     AddStorm(),
                                                     MoveCard(self.name, 'Hand', 'Graveyard')])
        self.add_mana_action(pyretic_ritual_action, paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

class DesperateRitual(Card):
    def __init__(self):
        super(DesperateRitual, self).__init__('Desperate Ritual')
        desperate_ritual_action = Action('Desperate Ritual',
                                         'Play',
                                         requirements=[CardInHand(self.name)],
                                         consequences=[AddMana({'Red': 3}),
                                                       AddStorm(),
                                                       MoveCard(self.name, 'Hand', 'Graveyard')])
        self.add_mana_action(desperate_ritual_action, paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

class RiteOfFlame(Card):
    def __init__(self):
        super(RiteOfFlame, self).__init__('Rite of Flame')
        rite_of_flame_action = Action('Rite of Flame',
                                      'Play',
                                      requirements=[CardInHand(self.name),
                                                    ManaInPool(ColorDict({'Red': 1}))],
                                      consequences=[MoveCard(self.name, 'Hand', 'Graveyard'),
                                                    ReduceMana(ColorDict({'Red': 1})),
                                                    AddStorm(),
                                                    AddRiteMana()])
        self.add_action(rite_of_flame_action)

class EmptyTheWarrens(Card):
    def __init__(self):
        super(EmptyTheWarrens, self).__init__('Empty the Warrens')
        empty_the_warrens_action = Action('Empty the Warrens',
                                          'Play',
                                          requirements=[CardInHand(self.name)],
                                          consequences=[AddStorm(),
                                                        AddGoblins(),
                                                        MoveCard(self.name, 'Hand', 'Graveyard')])
        self.add_mana_action(empty_the_warrens_action, paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 3})))

class GitaxianProbe(Card):
    def __init__(self):
        super(GitaxianProbe, self).__init__('Gitaxian Probe')
        gitaxian_probe_action = Action('Gitaxian Probe',
                                       'Play',
                                       requirements=[CardInHand(self.name)],
                                       consequences=[MoveCard(self.name, 'Hand', 'Graveyard'),
                                                     DrawCard(),
                                                     AddStorm()])
        self.add_action(gitaxian_probe_action)

class LandGrant(Card):
    def __init__(self):
        super(LandGrant, self).__init__('Land Grant')
        land_grant_action_land = Action('Land Grant',
                                        'Land',
                                        requirements=[CardNotInHand('Taiga'),
                                                      CardInHand(self.name),
                                                      CardInDeck('Taiga')],
                                        consequences=[MoveCard('Land Grant', 'Hand', 'Graveyard'),
                                                      MoveCard('Taiga', 'Deck', 'Hand'),
                                                      Shuffle(),
                                                      AddStorm()])
        land_grant_action_no_land = Action('Land Grant',
                                           'No land',
                                           requirements=[CardNotInHand('Taiga'),
                                                         CardInHand(self.name)],
                                           consequences=[MoveCard(self.name, 'Hand', 'Graveyard'),
                                                         Shuffle(),
                                                         AddStorm()])
        self.add_action(land_grant_action_land)
        self.add_action(land_grant_action_no_land)

class LionsEyeDiamond(Card):
    def __init__(self):
        super(LionsEyeDiamond, self).__init__('Lions Eye Diamond', is_permanent=True)
        lions_eye_diamond_play = Action('Lions Eye Diamond',
                                        'Play',
                                        requirements=[CardInHand(self.name)],
                                        consequences=[MoveCard(self.name, 'Hand', 'Battlefield'),
                                                      AddStorm()])
        lions_eye_diamond_activate = Action('Lions Eye Diamond',
                                            'Sacrifice',
                                            requirements=[CardInPlay(self.name)],
                                            consequences=[DiscardHand(),
                                                          MoveCard(self.name, 'Battlefield', 'Graveyard')])
        self.add_action(lions_eye_diamond_play)
        self.add_mana_action(lions_eye_diamond_activate, adding=[ColorDict({c: 3}) for c in COLORS])

class LotusPetal(Card):
    def __init__(self):
        super(LotusPetal, self).__init__('Lotus Petal', is_permanent=True)
        lotus_petal_play = Action('Lotus Petal',
                                  'Play',
                                  requirements=[CardInHand(self.name)],
                                  consequences=[MoveCard(self.name, 'Hand', 'Battlefield'),
                                                AddStorm()])
        lotus_petal_activate = Action('Lotus Petal',
                                      'Sacrifice',
                                      requirements=[CardInPlay(self.name)],
                                      consequences=[MoveCard(self.name, 'Battlefield', 'Graveyard')])
        self.add_action(lotus_petal_play)
        self.add_mana_action(lotus_petal_activate, adding=[ColorDict({c: 1}) for c in COLORS])

class Manamorphose(Card):
    def __init__(self):
        super(Manamorphose, self).__init__('Manamorphose')
        manamorphose_action = Action('Manamorphose',
                                     'Play',
                                     requirements=[CardInHand(self.name)],
                                     consequences=[MoveCard(self.name, 'Hand', 'Graveyard'),
                                                   DrawCard(),
                                                   AddStorm()])
        self.add_mana_action(manamorphose_action,
                                     paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})),
                                     adding=fill_up_remaining_colors(2, COLORS, ColorDict(), []))

class GoblinCharbelcher(Card):
    def __init__(self):
        super(GoblinCharbelcher, self).__init__('Goblin Charbelcher', is_tappable=True, is_permanent=True)
        charbelcher_play = Action('Goblin Charbelcher',
                                  'Play',
                                  requirements=[CardInHand(self.name)],
                                  consequences=[MoveCard(self.name, 'Hand', 'Battlefield'),
                                                AddStorm()])
        charbelcher_activate = Action('Goblin Charbelcher',
                                      'Activate',
                                      requirements=[CardInPlay(self.name),
                                                    CardUntapped(self.name)],
                                      consequences=[Tap(self.name),
                                                    Belch()])
        self.add_mana_action(charbelcher_play, paying=color_combinations(ColorDict({'Colorless': 4})))
        self.add_mana_action(charbelcher_activate, paying=color_combinations(ColorDict({'Colorless': 3})))

class ChromeMox(Card):
    def __init__(self):
        super(ChromeMox, self).__init__('Chrome Mox', is_tappable=True, is_permanent=True)
        for card_for_chrome_mox in CARDS_FOR_CHROME_MOX:
            chrome_mox_play = Action('Chrome Mox',
                                     'Play',
                                     requirements=[CardInHand(self.name),
                                                   CardInHand(card_for_chrome_mox)],
                                     consequences=[MoveCard(self.name, 'Hand', 'Battlefield'),
                                                   MoveCard(card_for_chrome_mox, 'Hand', 'Exile'),
                                                   AddStorm()])
            self.add_action(chrome_mox_play)
        chrome_mox_activate = Action('Chrome Mox',
                                     'Activate',
                                     requirements=[CardUntapped(self.name)],
                                     consequences=[Tap(self.name)])
        self.add_mana_action(chrome_mox_activate, adding=[ColorDict({c: 1}) for c in COLORS])

class BurningWish(Card):
    def __init__(self):
        super(BurningWish, self).__init__('Burning Wish')
        for card_for_burning_wish in CARDS_FOR_BURNING_WISH:
            burning_wish_wish = Action('Burning Wish',
                                       'Play ' + card_for_burning_wish,
                                       requirements=[CardInHand(self.name),
                                                     CardInSideboard(card_for_burning_wish)],
                                       consequences=[MoveCard(self.name, 'Hand', 'Exile'),
                                                     MoveCard(card_for_burning_wish, 'Sideboard', 'Hand'),
                                                     AddStorm()])
            self.add_mana_action(burning_wish_wish, paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

class ReforgeTheSoul(Card):
    def __init__(self):
        super(ReforgeTheSoul, self).__init__('Reforge the Soul')
        reforge_the_soul_action = Action('Reforge the Soul',
                                         'Play',
                                         requirements=[CardInHand(self.name)],
                                         consequences=[DiscardHand(),
                                                       DrawCard(7),
                                                       AddStorm()])
        self.add_mana_action(reforge_the_soul_action, paying=color_combinations(ColorDict({'Red': 2, 'Colorless': 3})))
