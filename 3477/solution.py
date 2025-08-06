class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        for fruit in fruits:
            found = False
            for j, basket in enumerate(baskets):
                if j not in used and fruit <= basket and not found:
                    used.add(j)
                    found = True
        return len(fruits) - len(used)