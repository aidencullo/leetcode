class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        if num1 >= num2:
            multiples = num1 // num2
            num1 %= num2
            return multiples + self.countOperations(num1, num2)
        else:
            multiples = num2 // num1
            num2 %= num1
            return multiples + self.countOperations(num1, num2)
