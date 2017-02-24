from numpy.random import choice

class Agent(object):
    def __init__(self, game_state):
        self.game_state = game_state

    def step(self):
        allowed, actions = self.game_state.possible_actions()
        actual_possible_actions = [action for legal, action in zip(allowed, actions) if legal == 1]
        action_to_take = choice(actual_possible_actions)
        #print(action_to_take)
        action_to_take.resolve(self.game_state)

    def run(self):
        for i in range(50):
            print(self.game_state)
            self.step()
        print(self.game_state)