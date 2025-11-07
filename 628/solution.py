class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        maximum_product = prod(nums[-3:])
        maximum_product = max(prod(nums[-2:]) * prod[-1])
        return maximum_product
        
