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

    def copy(self):
        return Action(self.requirements.copy(), self.consequences.copy())