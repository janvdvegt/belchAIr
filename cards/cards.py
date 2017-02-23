from mana_iterator import color_combinations, fill_up_remaining_colors
from requirements import ManaInPool, CardInHand, CardUntapped, CardInPlay, CardInSideboard, \
                         CardInDeck, CardNotInHand
from consequences import AddMana, MoveCard, Tap, AddStorm, AddRiteMana, AddGoblins, DrawCard, \
                         Shuffle, DiscardHand, Belch
from color_dict import ColorDict
from action import Action
from card import Card
from config import COLORS, CARDS_FOR_CHROME_MOX, CARDS_FOR_BURNING_WISH


seething_song = Card('Seething Song')
seething_song_action = Action(requirements=[CardInHand('Seething Song')],
                              consequences=[AddMana(ColorDict({'Red': 5})),
                                            MoveCard('Seething Song', 'Hand', 'Graveyard'),
                                            AddStorm()])
seething_song.add_mana_action(seething_song_action,
                              paying=color_combinations(ColorDict({'Red': 1,
                                                                   'Colorless': 2})))

class Taiga(Card):
    def __init__(self):
        super(Taiga, self).__init__('Taiga')

        taiga_action_play = Action(requirements=[CardInHand('Taiga')],
                                   consequences=[MoveCard('Taiga', 'Hand', 'Battlefield')])
        taiga_action_tap = Action(requirements=[CardUntapped('Taiga')],
                                  consequences=[Tap('Taiga')])
        self.add_action(taiga_action_play)
        self.add_mana_action(
            taiga_action_tap,
            adding=fill_up_remaining_colors(1, ['Red', 'Green'], ColorDict()))
class ElvishSpiritGuide(Card):
    def __init__(self):
        super(ElvishSpiritGuide, self).__init__('Elvish Spirit Guide')
        elvish_spirit_guide_action = Action(requirements=[CardInHand('Elvish Spirit Guide')],
                                            consequences=[AddMana(ColorDict({'Green': 1})),
                                                MoveCard('Elvish Spirit Guide', 'Hand', 'Exile')])
        self.add_action(elvish_spirit_guide_action)

class SimianSpiritGuide(Card):
    def __init__(self):
        super(SimianSpiritGuide, self).__init__('Simian Spirit Guide')
        simian_spirit_guide_action = Action(requirements=[CardInHand('Simian Spirit Guide')],
                                            consequences=[AddMana(ColorDict({'Red': 1})),
                                                  MoveCard('Simian Spirit Guide', 'Hand', 'Exile')])
        self.add_action(simian_spirit_guide_action)

tinder_wall = Card('Tinder Wall')
tinder_wall_play_action = Action(requirements=[CardInHand('Tinder Wall'),
                                               ManaInPool(ColorDict({'Green': 1}))],
                                 consequences=[MoveCard('Tinder Wall', 'Hand', 'Battlefield'),
                                               AddStorm()])
tinder_wall_mana_action = Action(requirements=[CardInPlay('Tinder Wall')],
                                 consequences=[MoveCard('Tinder Wall', 'Battlefield', 'Graveyard'),
                                               AddMana(ColorDict({'Red': 2}))])
tinder_wall.add_action(tinder_wall_play_action)
tinder_wall.add_action(tinder_wall_mana_action)

pyretic_ritual = Card('Pyretic Ritual')
pyretic_ritual_action = Action(requirements=[CardInHand('Pyretic Ritual')],
                               consequences=[AddMana({'Red': 3}),
                                             AddStorm(),
                                             MoveCard('Pyretic Ritual', 'Hand', 'Graveyard')])
pyretic_ritual.add_mana_action(pyretic_ritual_action,
                               adding=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

desperate_ritual = Card('Desperate Ritual')
desperate_ritual_action = Action(requirements=[CardInHand('Desperate Ritual')],
                                 consequences=[AddMana({'Red': 3}),
                                               AddStorm(),
                                               MoveCard('Desperate Ritual', 'Hand', 'Graveyard')])
desperate_ritual.add_mana_action(desperate_ritual_action,
                                 adding=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

rite_of_flame = Card('Rite of Flame')
rite_of_flame_action = Action(requirements=[CardInHand('Rite of Flame'),
                                            ManaInPool(ColorDict({'Red': 1}))],
                              consequences=[MoveCard('Rite of Flame', 'Hand', 'Graveyard'),
                                            AddStorm(),
                                            AddRiteMana()])
rite_of_flame.add_action(rite_of_flame_action)

empty_the_warrens = Card('Empty the Warrens')
empty_the_warrens_action = Action(requirements=[CardInHand('Empty the Warrens')],
                                  consequences=[AddStorm(),
                                                AddGoblins(),
                                                MoveCard('Empty the Warrens', 'Hand', 'Graveyard')])
empty_the_warrens.add_mana_action(empty_the_warrens_action,
                                  paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 3})))

gitaxian_probe = Card('Gitaxian Probe')
gitaxian_probe_action = Action(requirements=[CardInHand('Gitaxian Probe')],
                               consequences=[MoveCard('Gitaxian Probe', 'Hand', 'Graveyard'),
                                             DrawCard(),
                                             AddStorm()])
gitaxian_probe.add_action(gitaxian_probe_action)

land_grant = Card('Land Grant')
land_grant_action_land = Action(requirements=[CardInHand('Taiga'),
                                              CardInHand('Land Grant'),
                                              CardInDeck('Taiga')],
                                consequences=[MoveCard('Land Grant', 'Hand', 'Graveyard'),
                                              MoveCard('Taiga', 'Deck', 'Hand'),
                                              Shuffle(),
                                              AddStorm()])
land_grant_action_no_land = Action(requirements=[CardNotInHand('Taiga'),
                                                 CardInHand('Land Grant')],
                                   consequences=[MoveCard('Land Grant', 'Hand', 'Graveyard'),
                                                 Shuffle(),
                                                 AddStorm()])
land_grant.add_action(land_grant_action_land)
land_grant.add_action(land_grant_action_no_land)

lions_eye_diamond = Card('Lions Eye Diamond')
lions_eye_diamond_play = Action(requirements=[CardInHand('Lions Eye Diamond')],
                                consequences=[MoveCard('Lions Eye Diamond', 'Hand', 'Battlefield'),
                                              AddStorm()])
lions_eye_diamond_activate = Action(requirements=[CardInPlay('Lions Eye Diamond')],
                                    consequences=[DiscardHand(),
                                                  MoveCard('Lions Eye Diamond', 'Battlefield', 'Graveyard')])
lions_eye_diamond.add_action(lions_eye_diamond_play)
lions_eye_diamond.add_mana_action(lions_eye_diamond_activate,
                                  adding=[ColorDict({c: 3} for c in COLORS)])

lotus_petal = Card('Lotus Petal')
lotus_petal_play = Action(requirements=[CardInHand('Lotus Petal')],
                          consequences=[MoveCard('Lotus Petal', 'Hand', 'Battlefield'),
                                        AddStorm()])
lotus_petal_activate = Action(requirements=[CardInPlay('Lotus Petal')],
                              consequences=[MoveCard('Lotus Petal', 'Battlefield', 'Graveyard')])
lotus_petal.add_action(lotus_petal_play)
lotus_petal.add_mana_action(lotus_petal_activate,
                            adding=[ColorDict({c: 1} for c in COLORS)])

manamorphose = Card('Manamorphose')
manamorphose_action = Action(requirements=[CardInHand('Manamorphose')],
                             consequences=[MoveCard('Manamorphose', 'Hand', 'Graveyard'),
                                           DrawCard(),
                                           AddStorm()])
manamorphose.add_mana_action(manamorphose_action,
                             paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})),
                             adding=fill_up_remaining_colors(2, COLORS, ColorDict(), []))

goblin_charbelcher = Card('Goblin Charbelcher')
charbelcher_play = Action(requirements=[CardInHand('Goblin Charbelcher')],
                          consequences=[MoveCard('Goblin Charbelcher', 'Hand', 'Battlefield'),
                                        AddStorm()])
charbelcher_activate = Action(requirements=[CardInPlay('Goblin Charbelcher'),
                                            CardUntapped('Goblin Charbelcher')],
                              consequences=[Tap('Goblin Charbelcher'),
                                            Belch()])
goblin_charbelcher.add_mana_action(charbelcher_play,
                                   paying=color_combinations(ColorDict({'Colorless': 4})))
goblin_charbelcher.add_mana_action(charbelcher_activate,
                                   paying=color_combinations(ColorDict({'Colorless': 3})))

chrome_mox = Card('Chrome Mox')
for card_for_chrome_mox in CARDS_FOR_CHROME_MOX:
    chrome_mox_play = Action(requirements=[CardInHand('Chrome Mox'),
                                           CardInHand(card_for_chrome_mox)],
                             consequences=[MoveCard('Chrome Mox', 'Hand', 'Battlefield'),
                                           MoveCard(card_for_chrome_mox, 'Hand', 'Exile'),
                                           AddStorm()])
    chrome_mox.add_action(chrome_mox_play)
chrome_mox_activate = Action(requirements=[CardUntapped('Chrome Mox')],
                             consequences=[Tap('Chrome Mox')])
chrome_mox.add_mana_action(chrome_mox_activate, adding=[ColorDict({c: 1}) for c in COLORS])

burning_wish = Card('Burning Wish')
for card_for_burning_wish in CARDS_FOR_BURNING_WISH:
    burning_wish_wish = Action(requirements=[CardInHand('Burning Wish'),
                                             CardInSideboard(card_for_burning_wish)],
                               consequences=[MoveCard('Burning Wish', 'Hand', 'Exile'),
                                             MoveCard(card_for_burning_wish, 'Sideboard', 'Hand'),
                                             AddStorm()])
    burning_wish.add_mana_action(burning_wish_wish,
                                 paying=color_combinations(ColorDict({'Red': 1, 'Colorless': 1})))

reforge_the_soul = Card('Reforge the Soul')
reforge_the_soul_action = Action(requirements=[CardInHand('Reforge the Soul')],
                                 consequences=[DiscardHand(),
                                               DrawCard(7),
                                               AddStorm()])
reforge_the_soul.add_mana_action(reforge_the_soul_action,
                                 paying=color_combinations(ColorDict({'Red': 2, 'Colorless': 3})))
