class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        n = len(nums1)
        m = len(nums2)

        res = []

        while i < n and j < m:
            xi, x = nums1[i]
            yi, y = nums2[j]

            if xi == yi:
                res.append([xi, x + y])
                i += 1
                j += 1

            if yi < xi:
                res.append([yi, y])
                j += 1

            if xi < yi:
                res.append([xi, x])
                i += 1
        
        while i < n:
            res.append([xi, x])
            i += 1

        while j < m:
            res.append([yi, y])
            j += 1

        return res
