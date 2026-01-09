class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        values = list(cnt.values())
        gcd = values[0]
        for freq in values:
            gcd = math.gcd(gcd, freq)
        return gcd != 1
