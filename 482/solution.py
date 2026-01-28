class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = "".join(reversed(words))
        license = ""
        while characters:
            license += characters[:k]
            license += '-'
            characters = characters[k + 1:]
        return license[:-1]
