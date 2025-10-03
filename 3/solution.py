class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict

        seen = defaultdict(int)  # 1
        cleaned = []
        for num in nums:  # n
            if seen[num] < 3:
                seen[num] += 1
                cleaned.append(num)  # 1

        nums = cleaned
        nums.sort()  # nlgn

        indexes = defaultdict(int)

        for i, v in enumerate(nums):  # n
            indexes[v] += 1

        n = len(nums)
        result = []
        indexes_i = dict(indexes)
        for i in range(n):  # n
            indexes_i[nums[i]] -= 1
            indexes_j = dict(indexes_i)
            for j in range(i + 1, n):  # n
                indexes_j[nums[j]] -= 1
                target = nums[i] + nums[j]
                target *= -1

                if target in indexes_j and indexes_j[target]:
                    result.append([nums[i], nums[j], target])
        seen = set()
        result_unique = []
        for triple in result:  # n^3
            if tuple(triple) not in seen:
                seen.add(tuple(triple))
                result_unique.append(triple)
        return result_unique
