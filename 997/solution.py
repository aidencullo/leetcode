class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = set()
        trusted = defaultdict(int)
        for a, b in trust:
            trusts.add(a)
            trusted[b] += 1
            for person in trusted:
                if trusted[person] == n - 1 and person not in trusts:
                    return person
        return -1
