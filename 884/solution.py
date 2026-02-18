class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        res = []

        for word in c1:
            if c1.get(word) == 1 and word not in c2:
                res.append(word)


        for word in c2:
            if c2.get(word) == 1 and word not in c1:
                res.append(word)

        return res

