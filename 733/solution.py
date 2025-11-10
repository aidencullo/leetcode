class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(x, y, old_color):
            if not (0 <= x < n and 0 <= y < m):
                return

            if (x, y) in seen:
                return

            if image[x][y] != old_color:
                return

            image[x][y] = color
            seen.add((x, y))

            dfs(x + 1, y, old_color)
            dfs(x - 1, y, old_color)
            dfs(x, y + 1, old_color)
            dfs(x, y - 1, old_color)

            
            

            
        n = len(image)
        m = len(image[0])
        seen = set()
        dfs(sr, sc, image[sr][sc])
        return image
