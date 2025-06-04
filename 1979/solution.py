class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def getGCD(a, b):
            while a and b:
                smaller = min(a, b)
                larger = max(a, b)
                a, b = larger % smaller, smaller
            return max(a, b)

        smallest = min(nums)
        largest = max(nums)
        return getGCD(smallest, largest)
