class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        prefix = list(accumulate(arr))
        n = len(prefix)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if prefix[j] == 2 * prefix[i] and prefix[k] == 3 * prefix[i]:
                        return True
        return False
