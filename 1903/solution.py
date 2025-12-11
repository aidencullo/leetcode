class Solution:
    def largestOddNumber(self, num: str) -> str:
        def gen_substrings(s):
            return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        
        all_substrings = gen_substrings(num)
        largest = -math.inf
        for substring in all_substrings:
            x = int(substring)
            if x % 2 == 1:
                largest = max(largest, x)
        return "" if largest == -math.inf else str(largest)
