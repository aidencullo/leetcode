class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        c3 = c1 + c2
        return [k for k, v in c3.items() if v == 1]

