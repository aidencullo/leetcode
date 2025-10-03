from collections import Counter

# l = len(licensePlate)
# w = len(words)
# k = max(map(len, words))
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def remove_non_letters(word): # l time space
            word = word.lower() # l time space
            return [c for c in word if c.isalpha()] # l time space

        def is_subset(a, b):
            return not (a - b) # a time
        
        licensePlate_letters = remove_non_letters(licensePlate)
        licensePlate_counter = Counter(licensePlate_letters)
        shortest = math.inf
        res = []
        for word in words:
            word_counter = Counter(word)
            if is_subset(licensePlate_counter, word_counter):
                res.append(word)

        return min(res, key=len)

