class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        for x in nums2:
            if x in set1:
                return x
        return -1
