from numpy.random import choice

class Agent(object):
    def __init__(self, game_state, age=50):
        self.game_state = game_state
        self.age = age

    def step(self):
        allowed, actions = self.game_state.possible_actions()
        actual_possible_actions = [action for legal, action in zip(allowed, actions) if legal == 1]
        action_to_take = choice(actual_possible_actions)
        print(action_to_take)
        return action_to_take.resolve(self.game_state)

    def run(self):
        for i in range(self.age):
            print(self.game_state)
            self.step()
        print(self.game_state)
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
