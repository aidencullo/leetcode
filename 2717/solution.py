class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        n_i = nums.index(n)
        one_i = nums.index(1)
        moves = n - 1 - n_i + one_i
        if n_i < one_i:
            moves -= 1
        return moves
