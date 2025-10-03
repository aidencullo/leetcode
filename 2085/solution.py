class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter

        counter1 = Counter(words1)
        unique1 = {k for k, v in counter1.items() if v == 1}
        counter2 = Counter(words2)
        unique2 = {k for k, v in counter2.items() if v == 1}
        return len(unique1 & unique2)
