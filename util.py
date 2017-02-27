import numpy as np


def one_hot(x, cardinality):
    new_x = []
    for element in x:
        new_element = np.zeros(cardinality)
        new_element[element] = 1
        new_x.append(new_element)
    return np.array(new_x)