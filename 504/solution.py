class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        x = abs(num)
        sign = "" if num > 0 else "-"

        base_7 = []

        while x:
            x, digit = divmod(x, 7)
            base_7.append(str(digit))

        return sign + "".join(reversed(base_7))
    
