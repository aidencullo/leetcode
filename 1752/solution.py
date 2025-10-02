class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        min_value = min(nums)
        min_position = nums.index(min_value)

        i = min_position
        while nums[i - 1] == nums[i]:
            i -= 1
            i %= n
            if i == min_position:
                break
        min_position = i
            
        el = min_value
        for i in range(n):
            wrapped_i = ((i + min_position) % n)
            x = nums[wrapped_i]
            if x < el:
                return False
            el = x
        return True
            

            
