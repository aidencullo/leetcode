class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        prefix = list(accumulate(arr))
        n = len(prefix)
        for i in range(n):
            for j in range(i + 1, n - 1):
                if prefix[j] == 2 * prefix[i] and total == 3 * prefix[i]:
                        return True
        return False
