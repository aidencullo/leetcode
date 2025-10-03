class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter

        count1 = Counter(word1)
        count2 = Counter(word2)

        for key in count1:
            if abs(count1[key] - count2[key]) > 3:
                return False
        for key in count2:
            if abs(count1[key] - count2[key]) > 3:
                return False
        return True
