class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        def findSubsequence(i, sub_sequence):
            nonlocal min_subsequence
            if i == n:
                if sum(sub_sequence) <= sum(nums) / 2:
                    return
                if len(sub_sequence) > len(min_subsequence):
                    return
                if len(sub_sequence) == len(min_subsequence) and sum(sub_sequence) <= sum(min_subsequence):
                    return
                min_subsequence = sorted(sub_sequence, reverse=True)
                return
            
            num = nums[i]

            # if not sub_sequence:
            #     findSubsequence(i + 1, sub_sequence + [num])
            #     findSubsequence(i + 1, sub_sequence)

            # last = sub_sequence[-1]

            # if last >= num:
            #     return

            findSubsequence(i + 1, sub_sequence + [num])
            findSubsequence(i + 1, sub_sequence)
            

        n = len(nums)
        min_subsequence = [0] * n
        findSubsequence(0, [])
        return min_subsequence
        
