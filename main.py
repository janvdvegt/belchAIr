from cards.cards import *
from game_state import GameState
from agent import Agent
from netty_1 import Netty
from timeit import timeit
import numpy as np
from util import one_hot

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
print(taiga.is_tappable)

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
game_state.all_actions()

test_game_state = GameState()
test_game_state.add_card(taiga, 1, 0)
test_game_state.add_card(elvish_spirit_guide, 4, 0)
test_game_state.add_card(simian_spirit_guide, 4, 0)
test_game_state.add_card(tinder_wall, 4, 0)
test_game_state.add_card(desperate_ritual, 4, 0)
test_game_state.add_card(pyretic_ritual, 3, 0)
test_game_state.add_card(rite_of_flame, 4, 0)
test_game_state.add_card(seething_song, 4, 0)
test_game_state.add_card(empty_the_warrens, 3, 1)
test_game_state.add_card(gitaxian_probe, 4, 0)
test_game_state.add_card(land_grant, 4, 0)
test_game_state.add_card(lions_eye_diamond, 4, 0)
test_game_state.add_card(lotus_petal, 4, 0)
test_game_state.add_card(manamorphose, 2, 0)
test_game_state.add_card(goblin_charbelcher, 4, 0)
test_game_state.add_card(chrome_mox, 3, 0)
test_game_state.add_card(burning_wish, 4, 0)
test_game_state.add_card(reforge_the_soul, 0, 1)
test_game_state.reset_game(False)

#print(test_game_state.deck)
#print(test_game_state.hand)

#print(test_game_state.battlefield)
#legal_actions, all_actions = test_game_state.possible_actions()
#for legal_action, action in zip(legal_actions, all_actions):
#    if legal_action == 1:
#        print(action.card_name, ', ', action.action_name)

test_game_state.reduce_card_count('Rite of Flame', 'Deck')
test_game_state.reduce_card_count('Rite of Flame', 'Deck')
test_game_state.reduce_card_count('Seething Song', 'Deck')
test_game_state.reduce_card_count('Taiga', 'Deck')
test_game_state.reduce_card_count('Goblin Charbelcher', 'Deck')
test_game_state.reduce_card_count('Empty the Warrens', 'Deck')
test_game_state.reduce_card_count('Lions Eye Diamond', 'Deck')
test_game_state.increase_card_count('Rite of Flame', 'Hand')
test_game_state.increase_card_count('Rite of Flame', 'Hand')
test_game_state.increase_card_count('Seething Song', 'Hand')
test_game_state.increase_card_count('Taiga', 'Hand')
test_game_state.increase_card_count('Goblin Charbelcher', 'Hand')
test_game_state.increase_card_count('Empty the Warrens', 'Hand')
test_game_state.increase_card_count('Lions Eye Diamond', 'Battlefield')

# Passing turn (0)
# Playing Taiga (1)
# Lions Eye Diamond activate (24, 25)
# Belcher activate 40-43

#print(game_state.state_space())
#nlayers, nneurons, learning_rate, batch_size, number_batches, buffer_size, batch_games, epsilon
netty = Netty(game_state, 2, 64, 0.001, 512, 100, 200000, 500, 0.5, test_game_state)
netty.play_and_train()

"""netty = Netty(game_state, 2, 5, 0.001, 8, 100000, 500, 0.05)

action_taken = one_hot([0], netty.action_dim)

#print(netty.sess.run(netty.out_layer_sm, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
#                                                    netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
#print(netty.sess.run(netty.out_layer_sm_legal, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
#                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
#print(np.sum(netty.sess.run(netty.out_layer_sm, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
#                                                    netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]})))
#print(np.sum(netty.sess.run(netty.out_layer_masked, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
#                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]})))

print(netty.sess.run(netty.out_layer_sm_legal, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
print(netty.sess.run(netty.out_layer_masked_sm, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                                          netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))]}))
print(netty.sess.run(netty.loss, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                            netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))],
                                            netty.action_taken: action_taken}))

actions_taken, total_rewards_disc, legal_actions_list, state_inputs = netty.play_game()
print(actions_taken)
print(total_rewards_disc)
for legal_action in legal_actions_list:
    print(legal_action)
print(np.array(legal_actions_list).shape)
for state_input in state_inputs:
    print(state_input)
print(np.array(state_inputs).shape)"""

"""
losses = []
for i in range(1000):
    netty.sess.run(netty.train_op, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                              netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))],
                                              netty.action_taken: action_taken})
    cur_loss = netty.sess.run(netty.loss, feed_dict={netty.state_input: [np.ones(netty.game_state_dim)],
                                            netty.legal_actions: [np.concatenate((np.ones(20), np.zeros(netty.action_dim-20)))],
                                            netty.action_taken: action_taken})
    losses.append(cur_loss)
    if i % 25 == 0:
        print(cur_loss)

#losses = netty.train()
#print(losses)"""

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
