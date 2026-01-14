class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        indexes = {el: i for i, el in enumerate(order)}

        def compare(w1, w2):
            for c1, c2 in zip(w1, w2):
                if indexes[c1] < indexes[c2]:
                    return True
                if indexes[c1] > indexes[c2]:
                    return False
                # else equal, keep going
            # all equal so far → shorter word should come first
            return len(w1) <= len(w2)

        for a, b in pairwise(words):
            if not compare(a, b):
                return False
        return True
