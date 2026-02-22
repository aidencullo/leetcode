class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = -math.inf
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = max(product, math.prod(nums[i: j + 1]))
        return product
        
