class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        running_prod = 0
        max_prod = 0
        
        for num in nums:
            if running_prod <= 0:
                running_prod = num
            else:
                running_prod *= num
            max_prod = max(max_prod, running_prod)

        return max_prod
