class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_turbulence = 0
        running_turbulence = 0
        prev_cmp = 0

        for x, y in pairwise(arr):
            cur_cmp = (x > y) - (x < y)
            if cur_cmp == 0:
                running_turbulence = 0
            elif cur_cmp * prev_cmp == -1:
                running_turbulence += 1
            else:
                running_turbulence = 1
            prev_cmp = cur_cmp
            max_turbulence = max(max_turbulence, running_turbulence)

        return max_turbulence + 1
