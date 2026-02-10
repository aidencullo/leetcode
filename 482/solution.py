
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = []
        is_dash = lambda x: x == '-'
        from operator import not_
        is_not_dash = lambda x: not_(is_dash(x))
        s = ''.join(list(filter(s, is_not_dash)))
        cnt = (k - (len(s) % k)) % k
        for c in s:
            if cnt == k:
                cnt = 0
                license.append('-')
            license.append(c.upper())
            cnt += 1
        return ''.join(license)
