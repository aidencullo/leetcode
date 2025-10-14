class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        i = 0
        n = len(s)
        while i < n:
            end = i
            if i + k < n:
                start = i + k - 1
            else:
                start = n - 1
            res += s[end: start + 1][::-1]
            res += s[end + k: start + 1 + k]
            i += 2 * k
        return res
