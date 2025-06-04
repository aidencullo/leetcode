class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def getGCD(a, b):
            greatest = 1
            smallest = min(a, b)
            for i in range(2, smallest + 1):
                if a % i == 0 and b % i == 0:
                    greatest = i
            return greatest

        smallest = min(nums)
        largest = max(nums)
        return getGCD(smallest, largest)
