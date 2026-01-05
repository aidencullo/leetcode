class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        
        for i in range(x + 1):
            if i * i <= x:
                sqrt = i
            else:
                break

        return sqrt
