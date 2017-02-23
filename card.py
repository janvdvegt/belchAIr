from mana_iterator import color_combinations, fill_up_remaining_colors
from requirements import PayMana, InHand, InPlay, Untapped
from consequences import ReduceMana, AddMana, MoveCard, Tap, AddStorm
from color_dict import ColorDict
from action import Action


class Card(object):
    def __init__(self, name):
        self.name = name
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)


class SpellCard(Card):
    def __init__(self, name):
        super(SpellCard, self).__init__(name)

    def mana_cost_actions(self, mana_cost, action):
        for combination in color_combinations(mana_cost):
            next_action = action.copy()
            next_action.add_requirement(PayMana(combination))
            next_action.add_consequence(ReduceMana(combination))
            self.add_action(next_action)


class ManaGeneratingCard(Card):
    def __init__(self, name):
        super(ManaGeneratingCard, self).__init__(name)

    def mana_add_actions(self, action, amount_free, colors_free, colors_set):
        for combination in fill_up_remaining_colors(amount_free, colors_free,
                                                    colors_set, []):
            next_action = action.copy()
            next_action.add_consequence(AddMana(combination))
            self.add_action(next_action)


seething_song = SpellCard('Seething Song')
seething_song_action = Action(requirements=[InHand('Seething Song')],
                              consequences=[AddMana(ColorDict({'Red': 5})),
                                            MoveCard('Seething Song', 'Hand', 'Graveyard'),
                                            AddStorm()])
seething_song.mana_cost_actions(ColorDict({'Red': 1, 'Colorless': 2}),
                                seething_song_action)

taiga = ManaGeneratingCard('Taiga')
taiga_action_play = Action(requirements=[InHand('Taiga')],
                           consequences=[MoveCard('Taiga', 'Hand', 'Battlefield')])
taiga_action_tap = Action(requirements=[Untapped('Taiga')],
                          consequences=[Tap('Taiga')])
taiga.add_action(taiga_action_play)
taiga.mana_add_actions(taiga_action_tap, 1, ['Red', 'Green'], ColorDict())

elvish_spirit_guide = Card('Elvish Spirit Guide')
elvish_spirit_guide_action = Action(requirements=[InHand('Elvish Spirit Guide')],
                                    consequences=[AddMana(ColorDict({'Green': 1})),
                                                  MoveCard('Elvish Spirit Guide', 'Hand', 'Exile')])
elvish_spirit_guide.add_action(elvish_spirit_guide_action)

simian_spirit_guide = Card('Simian Spirit Guide')
simian_spirit_guide_action = Action(requirements=[InHand('Simian Spirit Guide')],
                                    consequences=[AddMana(ColorDict({'Red': 1})),
                                                  MoveCard('Simian Spirit Guide', 'Hand', 'Exile')])
simian_spirit_guide.add_action(simian_spirit_guide_action)

tinder_wall = Card('Tinder Wall')
tinder_wall_play_action = Action(requirements=[InHand('Tinder Wall'),
                                               PayMana(ColorDict({'Green': 1}))],
                                 consequences=[MoveCard('Tinder Wall', 'Hand', 'Battlefield'),
                                               AddStorm()])
tinder_wall_mana_action = Action(requirements=[InPlay('Tinder Wall')],
                                 consequences=[MoveCard('Tinder Wall', 'Battlefield', 'Graveyard'),
                                               AddMana(ColorDict({'Red': 2}))])
tinder_wall.add_action(tinder_wall_play_action)
tinder_wall.add_action(tinder_wall_mana_action)

pyretic_ritual = SpellCard('Pyretic Ritual')
pyretic_ritual_action = Action(requirements=[InHand('Pyretic Ritual')],
                               consequences=[AddMana({'Red': 3}),
                                             AddStorm(),
                                             MoveCard('Pyretic Ritual', 'Hand', 'Graveyard')])
pyretic_ritual.mana_cost_actions(ColorDict({'Red': 1, 'Colorless': 1}), pyretic_ritual_action)

desperate_ritual = SpellCard('Desperate Ritual')
desperate_ritual_action = Action(requirements=[InHand('Desperate Ritual')],
                                 consequences=[AddMana({'Red': 3}),
                                               AddStorm(),
                                               MoveCard('Desperate Ritual', 'Hand', 'Graveyard')])
desperate_ritual.mana_cost_actions(ColorDict({'Red': 1, 'Colorless': 1}), desperate_ritual_action)

rite_of_flame = Card('Rite of Flame')
rite_of_flame_action = Action(requirements=[InHand('Rite of Flame'),
                                            PayMana(ColorDict({'Red': 1}))],
                              consequences=[MoveCard('Rite of Flame', 'Hand', 'Graveyard'),
                                            AddStorm(),
                                            AddRiteMana()])
rite_of_flame.add_action(rite_of_flame_action)

empty_the_warrens = SpellCard('Empty the Warrens')
empty_the_warrens_action = Action(requirements=[InHand('Empty the Warrens')],
                                  consequences=[AddStorm(),
                                                AddGoblins(),
                                                MoveCard('Empty the Warrens', 'Hand', 'Graveyard')])
empty_the_warrens.mana_cost_actions(ColorDict({'Red': 1, 'Colorless': 3}), empty_the_warrens_action)

gitaxian_probe = Card('Gitaxian Probe')
gitaxian_probe_action = Action(requirements=[InHand('Gitaxian Probe')],
                               consequences=[MoveCard('Gitaxian Probe', 'Hand', 'Graveyard'),
                                             DrawCard(),
                                             AddStorm()])
gitaxian_probe.add_action(gitaxian_probe_action)

land_grant = Card('Land Grant')
land_grant_action_land = Action(requirements=[NotInHand('Taiga'),
                                              InHand('Land Grant'),
                                              InDeck('Taiga')],
                                consequences=[MoveCard('Land Grant', 'Hand', 'Graveyard'),
                                              MoveCard('Taiga', 'Deck', 'Hand'),
                                              Shuffle(),
                                              AddStorm()])
land_grant_action_no_land = Action(requirements=[NotInHand('Taiga'),
                                                 InHand('Land Grant')],
                                   consequences=[MoveCard('Land Grant', 'Hand', 'Graveyard'),
                                                 Shuffle(),
                                                 AddStorm()])
land_grant.add_action(land_grant_action_land)
land_grant.add_action(land_grant_action_no_land)

lions_eye_diamond = ManaGeneratingCard('Lions Eye Diamond')
lions_eye_diamond_play = Action(requirements=[InHand('Lions Eye Diamond')],
                                consequences=[MoveCard('Lions Eye Diamond', 'Hand', 'Battlefield'),
                                              AddStorm()])
lions_eye_diamond_activate = Action(requirements=[InPlay('Lions Eye Diamond')],
                                    consequences=[DiscardHand(),
                                                  MoveCard('Lions Eye Diamond', 'Battlefield', 'Graveyard')])
lions_eye_diamond.add_action(lions_eye_diamond_play)
####### OPLETTEN
lions_eye_diamond.mana_add_actions()

for a in taiga.actions:
    print(a.requirements, a.consequences)
