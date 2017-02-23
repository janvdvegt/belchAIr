# Action contains:
# - Requirements (mana, tapping, exiling a card from your hand etc)
# - Consequences to the environment / gamestate
# - A check whether the action is allowed given the requirements and the gamestate

from config import COLORS


class Action(object):
    def __init__(self, requirements=None, consequences=None):
        self.requirements = [] if requirements is None else requirements
        self.consequences = [] if consequences is None else consequences

    def allowed(self, game_state):
        for requirement in self.requirements:
            if not requirement.requirement_met(game_state):
                return False
        return True

    def add_requirement(self, requirement):
        self.requirements.append(requirement)

    def add_consequence(self, consequence):
        self.consequences.append(consequence)

    def copy(self):
        return Action(self.requirements.copy(), self.consequences.copy())
