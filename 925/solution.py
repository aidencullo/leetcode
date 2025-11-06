class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        from itertools import groupby
        name_grouped = [(k, len(list(g))) for k, g in groupby(name)]
        typed_grouped = [(k, len(list(g))) for k, g in groupby(typed)]

        if len(name_grouped) != len(typed_grouped):
            return False

        for (a, b), (c, d) in zip(name_grouped, typed_grouped):
            if a != c:
                return False
            if b > d:
                return False

        return True
            
        

# data = [1, 1, 2, 3, 3, 3, 2]
# grouped = [(k, list(g)) for k, g in groupby(data)]
# print(grouped)  # [(1, [1, 1]), (2, [2]), (3, [3, 3, 3]), (2, [2])]
