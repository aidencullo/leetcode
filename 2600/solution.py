class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if numOnes < k <= numOnes + numZeros:
            return numOnes
        if numOnes + numZeros <= k:
            return numOnes + min(k - numOnes - numZeros, numNegOnes) * -1
