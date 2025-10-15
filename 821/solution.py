class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [math.inf] * len(s)
        since_c = math.inf
        for i in range(len(s)):
            x = s[i]
            since_c += 1
            if x == c:
                since_c = 0
            answer[i] = min(answer[i], since_c)
        since_c = math.inf
        for i in range(len(s) - 1, -1, -1):
            x = s[i]
            since_c += 1
            if x == c:
                since_c = 0
            answer[i] = min(answer[i], since_c)
        return answer
            
