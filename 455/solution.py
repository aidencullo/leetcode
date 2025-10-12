class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = 0
        j = 0
        content_children = 0
        while j < len(s) and i < len(g):
            x = s[j]
            y = g[i]
            if x >= y:
                content_children += 1
                j += 1
                i += 1
            else:
                i += 1
        return content_children
                
