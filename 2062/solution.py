class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def is_vowel_substring(substring):
            return set(substring) == set('aeiou')

        vowel_substrings = 0
        n = len(word)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if is_vowel_substring(word[i: j]):
                    vowel_substrings += 1
        return vowel_substrings
