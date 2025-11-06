class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maximum_product = -math.inf
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                for k, z in enumerate(nums):
                    if i != j and j != k and i != k:
                        maximum_product = max(maximum_product, x * y * z)
        return maximum_product
