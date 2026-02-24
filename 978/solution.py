def cmp(a, b):
    return (a > b) - (a < b)

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_turbulence = 0
        running_turbulence = 0
        prev_cmp = 0

        for x, y in pairwise(arr):
            if cmp(x, y) == -1 and prev_cmp == 1:
                running_turbulence += 1
            if cmp(x, y) == 1 and prev_cmp == 1:
                running_turbulence = 1
            if cmp(x, y) == 1 and prev_cmp == -1:
                running_turbulence += 1
            if cmp(x, y) == -1 and prev_cmp == -1:
                running_turbulence = 1
            if cmp(x, y) == 0:
                running_turbulence = 0
            max_turbulence = max(max_turbulence, running_turbulence)
                

        return max_turbulence
