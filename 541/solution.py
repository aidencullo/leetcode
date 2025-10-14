class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def reverse_copy(start, end):
            l = end
            for j in range(start, end - 1, -1):
                res[l] = s[j]
                l += 1

        res = list(s)
        i = 0
        n = len(s)
        while i < n:
            end = i
            if i + k < n:
                start = i + k - 1
            else:
                start = n - 1
            reverse_copy(start, end)
            i += 2 * k
        return "".join(res)
