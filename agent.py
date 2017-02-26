from numpy.random import choice

class Agent(object):
    def __init__(self, game_state):
        self.game_state = game_state

    def step(self):
        allowed, actions = self.game_state.possible_actions()
        actual_possible_actions = [action for legal, action in zip(allowed, actions) if legal == 1]
        action_to_take = choice(actual_possible_actions)
        print(action_to_take)
        return action_to_take.resolve(self.game_state)

    def run(self):
        got_rewarded = False
        for i in range(5000):
            print(self.game_state)
            reward = self.step()
            if reward is not None:
                got_rewarded = True
                break
        print(self.game_state)
        print(reward)
        print(self.game_state.won)
        print(self.game_state.lost)
        print(got_rewarded)