from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        license_counter = Counter(c.lower() for c in licensePlate if c.isalpha())
        return min(
            (word for word in words if license_counter <= Counter(word.lower())),
            key=len
        )
