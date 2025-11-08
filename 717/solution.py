class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n:
            if i == n - 1:
                return True
            if bits[i] == 0:
                i += 1
                continue
            i += 2
        return False
