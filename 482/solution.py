class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = "".join(reversed(words))
        license = ""
        while characters:
            formatted_word = characters[-k:]
            formatted_words.app
        return license
