from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def remove_non_letters(word):
            word = word.lower()
            return [c for c in word if c.isalpha()]

        def is_subset(a, b):
            return not (a - b)
        
        licensePlate_letters = remove_non_letters(licensePlate)
        licensePlate_counter = Counter(licensePlate_letters)
        shortest = math.inf
        res = []
        for word in words:
            word_counter = Counter(word)
            if is_subset(licensePlate_counter, word_counter):
                res.append(word)

        return min(res, key=len)

