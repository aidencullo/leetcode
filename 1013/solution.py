class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg = sum(arr) / 3
        prefix = list(accumulate(arr))
        count = 0
        for x in prefix:
            print(x, avg, count)
            if x == avg or x == avg * 2:
                count += 1
        return count >= 2
