class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        stack = []
        min_sum = math.inf
        for num in nums:
            while stack and stack[-1] >= num:
                if len(stack) > 1 and stack[-1] > num:
                    min_sum = min(min_sum, stack[0] + stack[-1] + num)
                stack.pop()
            stack.append(num)
        return min_sum if min_sum != math.inf else -1
