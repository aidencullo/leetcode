class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_left = [0] + list(accumulate(nums))[:-1]
        prefix_right = list(reversed(list(accumulate(reversed(nums)))))[1:] + [0]
        n = len(nums)
        for i in range(n):
            if prefix_left[i] == prefix_right[i]:
                return i
        return -1
