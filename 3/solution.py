class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        from collections import defaultdict
        indexes = defaultdict(int)

        for i, v in enumerate(nums):
            indexes[v] += 1

        n = len(nums)
        result = []
        indexes_i = dict(indexes)
        for i in range(n):
            indexes_i[nums[i]] -= 1
            indexes_j = dict(indexes_i)
            for j in range(i + 1, n):
                indexes_j[nums[j]] -= 1
                target = nums[i] + nums[j]
                target *= -1

                if target in indexes_j and indexes_j[target]:
                    result.append([nums[i], nums[j], target])
        seen = set()
        result_unique = []
        for triple in result:
            if tuple(triple) not in seen:
                seen.add(tuple(triple))
                result_unique.append(triple)
        return result_unique
