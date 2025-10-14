class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = -1
        current = 0
        last_bit = -1
        substrings = 0
        for bit in s:
            if bit != last_bit:
                last = current
                current = 1
                last_bit = bit
            else:
                current += 1
            if current <= last:
                substrings += 1
        return substrings
