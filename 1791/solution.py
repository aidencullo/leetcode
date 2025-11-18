class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]

        if a == c:
            return a
        if a == d:
            return a
        return b
