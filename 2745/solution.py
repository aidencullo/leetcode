class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return 2 * (x + y + z)
        if x < y:
            return 2 * (2 * x + 1 + z)
        if x > y:
            return 2 * (2 * y + 1 + z)
