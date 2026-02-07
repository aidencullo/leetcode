class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cnt = 0
        license = []
        offset = len(s) % k
        cnt = (k - offset) % k
        s = [c for c in s if c != '-'

        for c in s:
            if c == '-':
                continue
            if cnt == k:
                cnt = 0
                license.append('-')
            cnt += 1
            license.append(c.upper())

        return ''.join(license)
            
