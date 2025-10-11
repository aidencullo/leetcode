class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(x):
            squares = 0
            y = x
            while y:
                squares += (y % 10) ** 2
                y //= 10
            return squares
        
        current = n
        seen = set()
        while current != 1:
            current = squares(current)
            if current in seen:
                return False
            seen.add(current)
        return True
        

s = Solution()
s.isHappy(2)
