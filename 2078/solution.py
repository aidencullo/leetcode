class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = -math.inf

        n = len(colors)

        for i, color in enumerate(colors):
            if color != colors[-1]:
                dist = max(dist, n - 1 - i)
                break

        for i, color in enumerate(reversed(colors)):
            if color != colors[0]:
                dist = max(dist, n - 1 - i)
                break

        return dist
