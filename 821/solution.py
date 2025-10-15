class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [math.inf] * len(s)
        since_c = math.inf
        cs = []
        for i, x in enumerate(s):
            if x == c:
                cs.append(i)
        for i, x in enumerate(s):
            answer[i] = min(abs(i - l) for l in cs)
        return answer
            
