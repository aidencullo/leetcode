class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = math.inf
        min_sum = math.inf
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    current_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(current_sum - target)
                    if diff < min_diff:
                        min_diff = diff
                        min_sum = current_sum
        return min_sum
            
