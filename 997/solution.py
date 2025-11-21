class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        is_trusted_by = defaultdict(int)
        trusts = defaultdict(int)
        for truster, trustee in trust:
            is_trusted_by[trustee] += 1
            trusts[truster] += 1
        for person in is_trusted_by:
            if is_trusted_by[person] == n - 1 and trusts[person] == 0:
                return person
        return -1
