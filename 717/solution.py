class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return False
        if len(bits) == 1:
            return True
        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        return self.isOneBitCharacter(bits[2:])
