class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def bin_search(start, end, target):
            l, r = start, end
            while l < r:
                k = (l + r) // 2
                if nums[k] == target:
                    return k
                if nums[k] > target:
                    r = k - 1
                else:
                    l = k + 1
            return l
            

        
        min_diff = math.inf
        min_sum = math.inf
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                start = j + 1
                end = n - 1
                resulting_sum = nums[i] + nums[j]
                val = target - resulting_sum
                k = bin_search(start, end, val)
                if k + 1 < n:
                    k += 1
                    current_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(current_sum - target)
                    if diff < min_diff:
                        min_diff = diff
                        min_sum = current_sum
                    k -= 1

                if k - 1 > j:
                    k -= 1
                    current_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(current_sum - target)
                    if diff < min_diff:
                        min_diff = diff
                        min_sum = current_sum
                    k += 1

                current_sum = nums[i] + nums[j] + nums[k]
                diff = abs(current_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    min_sum = current_sum
        return min_sum
            
