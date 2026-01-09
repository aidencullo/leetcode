class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return len(set((Counter(deck).values()))) == 1 and min(Counter(deck).values()) != 1
