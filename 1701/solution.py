class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(n, m):
            high, low = max(n, m), min(n, m)
            while low:
                low, high = high % low, low
            return high
        
        n = len(str1)
        m = len(str2)
        numeric_gcd = gcd(n, m)
        string_gcd = str1[:numeric_gcd]

        if string_gcd * (n // numeric_gcd) in str1 and
              string_gcd * (m // numeric_gcd) in str2:
                return string_gcd
        return ''
