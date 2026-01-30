class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        words = s.split('-')
        characters = "".join(words)
        characters = characters[::-1]
        characters = characters.upper()
        characters = characters[::-1]
        license = []
        offset = len(characters) % k
        i = 1 + offset
        while characters:
            if i % (k + 1) == 0:
                license.append('-')
            else:
                license.append(characters.pop())
            i += 1
        return ''.join(license)
