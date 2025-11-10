class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subsets(index, subset):
            if index == n:
                res.add(tuple(sorted(subset)))
                return

            subset.append(nums[index])
            subsets(index + 1, subset)
            subset.pop()
            subsets(index + 1, subset)

        n = len(nums)
        res = set()
        subsets(0, [])
        return [list(subset) for subset in res]
