from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from functools import cmp_to_key

        def compare(a, b):
            # return negative if a < b, zero if equal, positive if a > b

            if a not in arr2 and b not in arr2:
                return a - b

            if a not in arr2:
                return 1

            if b not in arr2:
                return -1

            return arr2.index(a) - arr2.index(b)

        return sorted(arr1, key=cmp_to_key(compare))


