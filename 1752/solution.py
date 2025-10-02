from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        new_nums = []
        seen = set()
        import math
        el = math.inf
        for x in nums:
            if x != el:
                new_nums.append(x)
            el = x
        new_new_nums = new_nums[-1:] + new_nums[:-1]

        min_val = min(new_new_nums)
        min_pos = new_new_nums.index(min_val)

        n = len(new_new_nums)
        for i in range(min_pos, n + min_pos - 1):
            i %= n
            j = (i + 1) % n
            if new_new_nums[i] > new_new_nums[j]:
                return False
        return True

s = Solution()
result = s.check([1] * 10)
print(result)
