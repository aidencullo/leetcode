from copy import deepcopy

lst = dir(1)
cpy = deepcopy(lst)
list1 = lst
list2 = cpy
# True
assert all(x is y for x, y in zip(list1, list2))


lst = dir(1)
lst.append([])
cpy = deepcopy(lst)
list1 = lst
list2 = cpy
# False
assert not all(x is y for x, y in zip(list1, list2))
