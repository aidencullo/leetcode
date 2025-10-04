from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:

        def remove_non_letters(word):
            lowercase_word = word.lower()
            only_letters = [c for c in lowercase_word if c.isalpha()]
            return only_letters

        def is_subset(a, b):
            return not (a - b)

        licensePlate_letters = remove_non_letters(licensePlate)
        licensePlate_counter = Counter(licensePlate_letters)
        res = []
        for word in words:
            word_counter = Counter(word)
            if is_subset(licensePlate_counter, word_counter):
                res.append(word)

        return min(res, key=len)
