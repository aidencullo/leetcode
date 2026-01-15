class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        items = defaultdict(int)
        
        for num in nums:
            if items[num] == 1:
                return num
            items[num] += 1
