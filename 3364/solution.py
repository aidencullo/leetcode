class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        import math
        minimum_sum = math.inf
        for subarray_length in range(l, r + 1):
            if subarray_length > n:
                break

            current_sum = sum(nums[i] for i  in range(subarray_length))
            if current_sum > 0:
                minimum_sum = min(minimum_sum, current_sum)

            i = 1
            while i + subarray_length - 1 < n:
                last_i = i - 1
                next_i = (i + subarray_length - 1)
                current_sum -= nums[last_i]
                current_sum += nums[next_i]
                if current_sum > 0:
                    minimum_sum = min(minimum_sum, current_sum)
                i += 1
            
        return minimum_sum if minimum_sum != math.inf else -1
