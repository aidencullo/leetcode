class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [math.inf] * len(s)
        since_c = math.inf
        cs = []
        for i, x in enumerate(s):
            if x == c:
                cs.append(i)
        cs.sort()
        import bisect

        def get_closest_index(index):
            i = bisect.bisect(cs, index)
            if i == 0:
                return cs[0]
            if i == len(cs):
                return cs[len(cs) - 1]
            if abs(cs[i] - index) < abs(cs[i - 1] - index):
                return cs[i]
            return cs[i - 1]
        
        for i, x in enumerate(s):
            c_i = get_closest_index(i)
            answer[i] = abs(i - c_i)
        return answer
            
