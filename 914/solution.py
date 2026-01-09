class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        values = cnt.values()
        return reduce(gcd, values) != 1
