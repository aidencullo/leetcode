from collections import Counter

# l = len(licensePlate)
# w = len(words)
# k = max(map(len, words))
# l + w(k + l) ) + w = l + wk + wl + w = w(l + k) time
# l + l + k + l + w = l + k + w space
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def remove_non_letters(word): # l time space
            lowercase_word = word.lower() # l time space
            only_letters = [c for c in lowercase_word if c.isalpha()] # l time space
            return only_letters

        def is_subset(a, b):
            return not (a - b) # a time
        
        licensePlate_letters = remove_non_letters(licensePlate) # l timespace
        licensePlate_counter = Counter(licensePlate_letters) # l timespace
        shortest = math.inf # 1 timespace
        res = [] # 1 timespace
        for word in words: # w time 1 space
            word_counter = Counter(word) # k timespace
            if is_subset(licensePlate_counter, word_counter): # l timespace
                res.append(word) # 1 time, w space (worst case)

        return min(res, key=len) # w

