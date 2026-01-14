class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        def compare(w1, w2):
            return [order.index(c) for c in w1] <= [order.index(c) for c in w2]
        
        for a, b in pairwise(words):
            if not compare(a, b):
                return False
        return True
