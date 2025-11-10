class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets(index, subset):
            if index == n:
                res.append(subset)
                return

            subsets(index + 1, subset + [nums[index]])
            subsets(index + 1, subset)

        n = len(nums)
        res = []
        subsets(0, [])
        return res
