class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def getGCD(small, large):
            while small:
                large, small = small, large % small
            return large

        smallest = min(nums)
        largest = max(nums)
        return getGCD(smallest, largest)
