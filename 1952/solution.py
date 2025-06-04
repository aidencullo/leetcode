class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1 or n == 2:
            return False
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return int(math.sqrt(n)) == math.sqrt(n)
