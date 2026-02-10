class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = []
        is_dash = lambda x: x == '-'
        s = ''.join([c for c in s if not is_dash])
        cnt = (k - (len(s) % k)) % k
        for c in s:
            if cnt == k:
                cnt = 0
                license.append('-')
            license.append(c.upper())
            cnt += 1
        return ''.join(license)
