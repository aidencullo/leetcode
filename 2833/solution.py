class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        m = -math.inf
        left = 0
        right = 0

        for c in moves:
            if c == 'L' or c == '-':
                left += 1
            else:
                left -= 1
            m = max(m, left)

        for c in moves:
            if c == 'R' or c == '-':
                right += 1
            else:
                right -= 1
            m = max(m, right)

        return m
