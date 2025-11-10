class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix_left = [0] + list(accumulate(nums))[:-1]
        prefix_right = list(reversed(list(accumulate(reversed(nums)))))[1:] + [0]
        n = len(nums)
        return [abs(prefix_left[i] - prefix_right[i]) for i in range(n)]
