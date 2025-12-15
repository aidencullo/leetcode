class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for x in range(1, num + 1):
            if x * x > num:
                return False
            if num == x * x:
                return True
