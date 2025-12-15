class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for x in range(num):
            if num == x * x:
                return True
        return False
