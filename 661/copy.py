from copy import deepcopy, copy

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

a = [0]
lst = [[a]]
lst
cpy = deepcopy(lst)
a[0] = 1
assert lst[0][0][0] == 1
assert cpy[0][0][0] == 0


a = [0]
lst = [[a]]
lst
cpy = copy(lst)
a[0] = 1
assert lst[0][0][0] == 1
assert cpy[0][0][0] == 1
