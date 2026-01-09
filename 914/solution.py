class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        if min(Counter(deck).values()) == 1:
            return False
        min_freq = min(Counter(deck).values())
        gcd = min_freq
        for freq in Counter(deck).values():
            gcd = math.gcd(gcd, freq)
        return gcd != 1
