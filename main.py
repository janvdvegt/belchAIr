from cards.cards import *
from game_state import GameState
from agent import Agent
from netty_1 import Netty
from timeit import timeit
import numpy as np

taiga = Taiga()
elvish_spirit_guide = ElvishSpiritGuide()
simian_spirit_guide = SimianSpiritGuide()
tinder_wall = TinderWall()
desperate_ritual = DesperateRitual()
pyretic_ritual = PyreticRitual()
rite_of_flame = RiteOfFlame()
seething_song = SeethingSong()
empty_the_warrens = EmptyTheWarrens()
gitaxian_probe = GitaxianProbe()
land_grant = LandGrant()
lions_eye_diamond = LionsEyeDiamond()
lotus_petal = LotusPetal()
manamorphose = Manamorphose()
goblin_charbelcher = GoblinCharbelcher()
chrome_mox = ChromeMox()
burning_wish = BurningWish()
reforge_the_soul = ReforgeTheSoul()

game_state = GameState()
game_state.add_card(taiga, 1, 0)
game_state.add_card(elvish_spirit_guide, 4, 0)
game_state.add_card(simian_spirit_guide, 4, 0)
game_state.add_card(tinder_wall, 4, 0)
game_state.add_card(desperate_ritual, 4, 0)
game_state.add_card(pyretic_ritual, 3, 0)
game_state.add_card(rite_of_flame, 4, 0)
game_state.add_card(seething_song, 4, 0)
game_state.add_card(empty_the_warrens, 3, 1)
game_state.add_card(gitaxian_probe, 4, 0)
game_state.add_card(land_grant, 4, 0)
game_state.add_card(lions_eye_diamond, 4, 0)
game_state.add_card(lotus_petal, 4, 0)
game_state.add_card(manamorphose, 2, 0)
game_state.add_card(goblin_charbelcher, 4, 0)
game_state.add_card(chrome_mox, 3, 0)
game_state.add_card(burning_wish, 4, 0)
game_state.add_card(reforge_the_soul, 0, 1)
game_state.reset_game()
game_state.draw_opening_hand()

print(game_state.state_space())

netty = Netty(game_state, 2, 5, 0.001, 8, 0.05)
netty.build_model()
print(netty.sess.run(netty.out_layer_sm, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                    netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
print(netty.sess.run(netty.out_layer_sm_legal, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
print(np.sum(netty.sess.run(netty.out_layer_sm, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                    netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]})))
print(np.sum(netty.sess.run(netty.out_layer_sm_legal, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]})))


losses = netty.train()
print(losses)

"""agent = Agent(game_state)
agent.run()


def run_game():
    game_state.reset_game()
    game_state.draw_opening_hand()
    agent = Agent(game_state)
    agent.run()"""

"""
game_state.increase_card_count('Lions Eye Diamond', 'Hand')
game_state.reduce_card_count('Lions Eye Diamond', 'Deck')
#print(game_state.deck)
print(game_state.hand)
possible_actions, all_actions = game_state.possible_actions()
possible_actions = [action for action, legal in zip(all_actions, possible_actions) if legal == 1]

done = False
for action in possible_actions:
    for con in action.consequences:
        print(type(con))
        if isinstance(con, MoveCard):
            if con.card == 'Lions Eye Diamond':
                action.resolve(game_state)
                done = True
                break
    if done:
        break

print(done)
print(game_state.hand)
print(game_state.battlefield)
possible_actions, all_actions = game_state.possible_actions()
possible_actions = [action for action, legal in zip(all_actions, possible_actions) if legal == 1]

done = False
for action in possible_actions:
    for con in action.consequences:
        print(type(con))
        if isinstance(con, DiscardHand):
            action.resolve(game_state)
            done = True
            break
    if done:
        break

print(done)
print(game_state.hand)
print(game_state.battlefield)

print(len(game_state.state_space()))
print(game_state.state_space())


#print(sum([game_state.deck[k] for k in game_state.deck]))
#print(sum([game_state.sideboard[k] for k in game_state.sideboard]))
#print(len(game_state.all_actions()))
"""
