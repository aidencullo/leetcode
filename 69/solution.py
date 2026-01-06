class Solution:
    def mySqrt(self, x: int) -> int:
        """
        LeetCode 69: Sqrt(x)
        Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
        """
        largest_sqrt = 1
        
        for y in range(1, x + 1):
            if y ** 2 <= x:
                largest_sqrt = y

        return largest_sqrt
