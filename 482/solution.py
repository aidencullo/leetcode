class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = []
        cnt = 0
        for c in reversed(s):
            if c == '-':
                continue
            if cnt == k:
                cnt = 0
                license.append('-')
            license.append(c.upper())
            cnt += 1
        return ''.join(reversed(license))
