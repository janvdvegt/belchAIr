from mana_iterator import color_combinations, fill_up_remaining_colors
from requirements import ManaInPool
from consequences import ReduceMana, AddMana, MoveCard, Tap, AddStorm
from color_dict import ColorDict
from action import Action


class Card(object):
    """
    Card object
    """
    def __init__(self, name, tappable=False):
        self.name = name
        self.actions = []
        self.tappable = tappable

    def add_action(self, action):
        """
        Accessor for adding actions to private list.
        :param action Action
        :return: None
        Should this return current actions?
        """
        self.actions.append(action)

    def add_mana_action(self, action, paying=None, adding=None):
        """
        Can the paying and adding dicts be checked in a more concise manner?
        Maybe add a method to ColorDict
        :param action Action
        :param paying ColorDict
        :param adding ColorDict
        :return: None
        """
        if isinstance(paying, ColorDict):
            paying = [paying]
        if isinstance(adding, ColorDict):
            adding = [adding]
        #Should this be if paying and not adding
        if paying is not None and adding is None:
            for option in paying:
                next_action = action.copy()
                next_action.add_requirement(ManaInPool(option))
                next_action.add_consequence(ReduceMana(option))
                self.add_action(next_action)
        #Should this be if not paying and adding
        elif paying is None and adding is not None:
            for option in adding:
                next_action = action.copy()
                next_action.add_consequence(AddMana(option))
                self.add_action(next_action)
        #Should this be if not paying and adding
        elif paying is not None and adding is not None:
            for option_add in adding:
                for option_pay in paying:
                    next_action = action.copy()
                    next_action.add_requirement(ManaInPool(option_pay))
                    next_action.add_consequence(ReduceMana(option_pay))
                    next_action.add_consequence(AddMana(option_add))
                    self.add_action(next_action)
