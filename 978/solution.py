class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        down = up = max_turbulence = 1

        for x, y in pairwise(arr):
            cur_cmp = (x > y) - (x < y)

            if cur_cmp == -1:
                up = down + 1
                down = 1
            elif cur_cmp == 1:
                down = up + 1
                up = 1
            else:
                down = 1
                up = 1

            max_turbulence = max(up, down, max_turbulence)

        return max_turbulence
