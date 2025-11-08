from copy import copy, deepcopy

class Human:
    def __init__(self, name):
        self.name = name

humans = [Human("Alice"), Human("Bob")]

shallow = copy(humans)      # new list, same Human objects
deep = deepcopy(humans)     # new list, copies of Human objects

assert shallow[0] is humans[0]     # True
assert deep[0] is not humans[0]        # False
