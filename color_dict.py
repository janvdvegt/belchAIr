from collections import defaultdict


class ColorDict(defaultdict):
    def __init__(self, c_dict=None):
        super(ColorDict, self).__init__(int)
        if c_dict is not None:
            for k in c_dict:
                self[k] = c_dict[k]

    def add_mana(self, c_dict):
        for k in c_dict:
            self[k] += c_dict[k]

    def copy(self):
        c_dict = defaultdict(int)
        for k in self:
            c_dict[k] = self[k]
        new_color_dict = ColorDict(c_dict)
        return new_color_dict
