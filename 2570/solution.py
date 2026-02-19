class Solution:
    def mergeArrays(self, nums1, nums2):
        return sorted((Counter(dict(nums1)) + Counter(dict(nums2))).items())
