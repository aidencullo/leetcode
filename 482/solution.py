class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cnt = 0
        license = []

        for c in reversed(s):
            if c == '-':
                continue
            if cnt == k:
                cnt = 0
                license.append('-')
            cnt += 1
            license.append(c)

        return ''.join(reversed(license))
            
