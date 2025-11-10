class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg = sum(arr) / 3
        prefix = list(accumulate(arr))
        count = 0
        first = False
        for x in prefix[:-1]:
            if first and x == avg * 2:
                return True
            if x == avg:
                first = True
        return False
