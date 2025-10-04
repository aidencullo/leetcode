from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        def remove_non_letters(word: str):
            lowercase = word.lower()
            letters = list(filter(str.isalpha, lowercase))
            return letters

        def is_subset(a: Counter[str], b: Counter[str]) -> bool:
            return a <= b

        licensePlate_letters = remove_non_letters(licensePlate)
        licensePlate_counter = Counter(licensePlate_letters)
        res = []
        for word in words:
            word_counter = Counter(word)
            if is_subset(licensePlate_counter, word_counter):
                res.append(word)

        return min(res, key=len)
