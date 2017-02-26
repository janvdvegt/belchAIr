# Action contains:
# - Requirements (mana, tapping, exiling a card from your hand etc)
# - Consequences to the environment / gamestate
# - A check whether the action is allowed given the requirements and the gamestate

from config import COLORS


class Action(object):
    """
    Action Class, gathers requirements and consequences.
    """
    def __init__(self, requirements=None, consequences=None):
        self.requirements = requirements if requirements else []
        self.consequences = consequences if consequences else []

    def allowed(self, game_state):
        # If this action is not allowed return False
        return all([requirement.requirement_met(game_state) for requirement in self.requirements])

    def add_requirement(self, requirement):
        self.requirements.append(requirement)

    def add_consequence(self, consequence):
        self.consequences.append(consequence)

    def resolve(self, game_state):
        for consequence in self.consequences:
            reward = consequence.resolve(game_state)
            if reward is not None:
                return reward

    def copy(self):
        return Action(self.requirements.copy(), self.consequences.copy())

    def __str__(self):
        str_repr = 'Requirements:\n'
        for req in self.requirements:
            str_repr += '   ' + str(req) + '\n'
        str_repr += 'Consequences:\n'
        for con in self.consequences:
            str_repr += '   ' + str(con) + '\n'
        return str_repr
