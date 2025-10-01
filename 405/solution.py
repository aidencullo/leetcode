class Solution:
    def toHex(self, num: int) -> str:
        def decToHex(num):
            if num == 0:
                return 0
            res = ''
            while num:
                remainder = num % 16
                if remainder < 10:
                    res += str(num % 16) 
                elif remainder == 10:
                    res += 'a'       
                elif remainder == 11:
                    res += 'b'       
                elif remainder == 12:
                    res += 'c'       
                elif remainder == 13:
                    res += 'd'       
                elif remainder == 14:
                    res += 'e'       
                elif remainder == 15:
                    res += 'f'       
                num //= 16
            return res[::-1]
        
        if num >= 0:
            return decToHex(num)
        magnitude = num if num > 0 else -num
        invert = ~magnitude & 0xffffffff
        plus_one = invert + 1
        hexadecimal = decToHex(plus_one)
        return hexadecimal
