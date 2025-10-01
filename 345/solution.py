VOWELS = set('aeiouAEIOU')


class Solution:
    def reverseVowels(self, s: str) -> str:

        def is_vowel(c):
            return c in VOWELS
        
        vowels = []
        for c in s:
            if is_vowel(c):
                vowels.append(c)

        res = []
        for c in s:
            if is_vowel(c):
                res.append(vowels.pop())
            else:
                res.append(c)
        return ''.join(res)
