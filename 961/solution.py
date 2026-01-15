class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        items = {}
        
        for num in nums:
            if items.get(num) == 1:
                return num
            items[num] = items.get(num, 0) + 1
