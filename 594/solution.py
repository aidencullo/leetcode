class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lhs = 0
        for x in nums:
            count = 0
            atleast = 0
            for y in nums:
                if x - y == 1:
                    atleast = 1
                    count += 1
                if x - y == 0:
                    count += 1
            if atleast:
                lhs = max(lhs, count)
            count = 0
            atleast = 0
            for y in nums:
                if y - x == 1:
                    atleast = 1
                    count += 1
                if y - x == 0:
                    count += 1
            if atleast:
                lhs = max(lhs, count)
        return lhs
            
