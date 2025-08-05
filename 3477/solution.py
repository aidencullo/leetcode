class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        for fruit in fruits:
            for j, basket in enumerate(baskets):
                if j not in used and fruit <= basket:
                    used.add(j)
        return len(fruits) - len(used)