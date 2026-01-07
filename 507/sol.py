"""
LeetCode Problem 507: Perfect Number

https://leetcode.com/problems/perfect-number/

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        divisors = [i for i in range(1, num) if num % i == 0]
        
        def helper(current):
            if current == 0:
                return True
            if current < 0:
                return False
            return any(helper(current - d) for d in divisors)

        return helper(num)
