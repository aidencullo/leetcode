VOWELS = set("aeiouAEIOU")


class Solution:
    def reverse_vowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c in VOWELS

        vowels = [c for c in s if is_vowel(c)]

        return "".join(vowels.pop() if is_vowel(c) else c for c in s)
