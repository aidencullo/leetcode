class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = ''.join(words)
        characters = characters.upper()
        characters = list(characters)
        license = []
        n = len(characters)
        offset = k - (n % k)
        i = 1 + offset
        while characters:
            if i % (k + 1) == 0:
                license.append('-')
            else:
                license.append(characters.pop(0))
            i += 1
        return ''.join(license)
