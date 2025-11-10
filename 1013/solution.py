class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        prefix = list(accumulate(arr))
        n = len(prefix)
        seen = set()
        for x in prefix[:-1]:
            if x / 2 in seen and x / 2 == total - x:
                return True
            seen.add(x)
        return False
