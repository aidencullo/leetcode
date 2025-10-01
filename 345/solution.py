class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = [] # 1 time space
        for c in s: # n time
            if c in 'aeiouAEIOU': # 1 time space
                vowels.append(c) # 1 time, agg n space

        res = []
        for c in s: # n time
            if c in 'aeiouAEIOU': # 1 time space
                res.append(vowels.pop()) # 1 time n space agg
            else:
                res.append(c) # n space agg, 1 time
        return ''.join(res) # n time space
