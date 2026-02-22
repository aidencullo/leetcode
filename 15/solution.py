class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = nums
        res = []
        seen = set()
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                complement = -arr[i] - arr[j]
                if complement in seen:
                    res.append([arr[i], arr[j], complement])
            seen.add(nums[i])


                        
        return [list(t) for t in set(tuple(l) for l in res)]
