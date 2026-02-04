class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = ''.join(words)
        characters = characters.upper()
        characters = list(characters)
        license = []
        n = len(characters)
        offset = n % k
        i = 0
        while characters:
            if i != 0and i % k == offset:
                license.append('-')
            license.append(characters.pop(0))
            i += 1
        return ''.join(license)
