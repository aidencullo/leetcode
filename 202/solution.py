class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(x):
            squares = 0
            y = x
            while y:
                squares += (y % 10) ** 2
                y //= 10
            return squares
        
        runner = n
        double_runner = squares(n)
        seen = set()
        while runner != 1:
            if runner == double_runner:
                return False
            runner = squares(runner)
            double_runner = squares(squares(double_runner))
        return True
