'''
time
nm

space
nm
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return
            
            if (r, c) in seen:
                return

            if image[r][c] != old_color:
                return

            seen.add((r, c))
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            

        n = len(image)
        m = len(image[0])
        seen = set()
        old_color = image[sr][sc]
        dfs(sr, sc)
        return image
