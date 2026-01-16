class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def helper(i, remaining, lst):
            if remaining == 0:
                combinations.append(lst)
                return

            if i == n + 1:
                return

            helper(i + 1, remaining - 1, lst + [i])
            helper(i + 1, remaining, lst)
            

        helper(1, k, [])
        return combinations
