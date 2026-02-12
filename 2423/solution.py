class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        if set(cnt.values()) != 2:
            return False
