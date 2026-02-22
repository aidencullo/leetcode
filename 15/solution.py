from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = nums
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == 0:
                        res.append([arr[i], arr[j], arr[k]])
        return res
