from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0

        while candies:
            print(res)
            share = min(candies, i + 1)
            candies -= share
            res[i % num_people] += share
            i += 1

        return res
