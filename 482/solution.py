class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = "".join(words)
        characters = characters[::-1]
        characters = characters.upper()
        license = ""
        while characters:
            license += characters[:k]
            license += '-'
            characters = characters[k:]
        return license[:-1][::-1]
