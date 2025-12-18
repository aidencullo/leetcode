class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, combination):
            combination_sum = sum(combination)

            if combination_sum == target:
                combinations.add(tuple(combination))

            if i == len(candidates):
                return

            if combination_sum > target:
                return

            backtrack(i + 1, combination + [candidates[i]])
            backtrack(i + 1, combination)

        candidates.sort()
        combinations = set()
        backtrack(0, [])
        return [list(t) for t in combinations]
