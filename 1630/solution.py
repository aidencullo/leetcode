class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(s): # O(n)
            if len(s) < 2:
                return False
            return all(s[i + 1] - s[i] == s[1] - s[0] for i in range(len(s) - 1))
        
        def is_arithmetic_subarray(i, j):
            lst  = list(islice(nums, i, j + 1))
            lst.sort() # O(nlgn)
            return is_arithmetic(lst)
        
        answer = []
        for (start_index, end_index) in zip(l, r):
            answer.append(is_arithmetic_subarray(start_index, end_index))
        return answer
        
