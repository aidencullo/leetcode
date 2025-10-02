class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        el = nums[-1]
        for x in nums:
            if x < el:
                count += 1
                if count > 1:
                    return False
            el = x
        return True
