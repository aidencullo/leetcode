class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            seen = set()
            res = set()
            for x in nums:
                if target - x in seen:
                    res.add(tuple(sorted((x, target - x))))
                seen.add(x)
            return list(list(l) for l in res)
                
        
        result = set()
        n = len(nums)
        for i in range(n):
            remaining = nums[:i] + nums[i + 1:]
            twoSums = twoSum(remaining, -nums[i])
            for p1, p2 in twoSums:                
                throuple = tuple(sorted((p1, p2, nums[i])))
                if throuple not in result:
                    result.add(throuple)
        return list(map(list, result))
