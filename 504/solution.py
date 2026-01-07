class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        x = num if num > 0 else -num

        i = 0
        base_7 = 0

        while x:
            x, digit = divmod(x, 7)
            base_7 += digit * 10 ** i
            i += 1

        base_7 = base_7 if num > 0 else -base_7
        return str(base_7)
    
