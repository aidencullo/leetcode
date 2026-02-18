class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_values = set(nums1) & set(nums2)
        return min(common_values) if common
