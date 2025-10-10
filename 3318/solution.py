class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def findXSum(nums: List[int], x: int) -> List[int]:
            from collections import Counter
            nums.sort(reverse=True)
            c = Counter(nums)
            return sum(k * v for k, v in c.most_common(x))
            
        n = len(nums)
        return [findXSum(nums[i: i + k - 1 + 1], x) for i in range(n - k + 1)]
