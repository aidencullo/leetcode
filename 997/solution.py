class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = set()
        trusted = defaultdict(int)
        for i in range(1, n + 1):
            trusted[i] = 0
        for a, b in trust:
            trusts.add(a)
            trusted[b] += 1
        for person in trusted:
            if trusted[person] == n - 1 and person not in trusts:
                return person
        return -1
