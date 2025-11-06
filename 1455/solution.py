class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        return next((i + 1 for i, word in enumerate(words) if word.startswith(searchWord)), -1)
