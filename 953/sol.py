class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        indexes = {el: i for i, el in enumerate(order)}

        def compare(w1, w2):
            return [indexes[c] for c in w1] <= [indexes[c] for c in w2]

        
        for a, b in pairwise(words):
            if not compare(a, b):
                return False
        return True
