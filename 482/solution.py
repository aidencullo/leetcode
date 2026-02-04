class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = ''.join(words)
        characters = characters.upper()
        characters = list(characters)
        characters.reverse()
        license = []
        n = len(characters)
        offset = n % k
        i = 0
        while characters:
            if i != 0 and i % k == offset:
                license.append('-')
            license.append(characters.pop())
            i += 1
        return ''.join(license)
