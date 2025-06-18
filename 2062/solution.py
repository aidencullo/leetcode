class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def is_vowel_substring(start, end):
            return set(word[start: end + 1]) == set("aeiou")

        def is_vowel(index):
            return word[index] in "aeiou"
        
        l, m, r = 0, 0, 0
        n = len(word)
        vowel_substrings = 0
        while m < n:
            while m < n and not is_vowel(m):
                m += 1
                l = m
                r = m
            while m < n and not is_vowel_substring(l, m):
                m += 1
            r = m
            while r < n and is_vowel(r):
                vowel_substrings += 1
                r += 1
            l += 1
        return vowel_substrings
