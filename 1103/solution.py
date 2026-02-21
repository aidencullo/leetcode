from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0

        while candies:
            share = min(candies, i + 1)
            candies -= share
            res[i] += share
            i = (i + 1) % num_people
            

        return res
