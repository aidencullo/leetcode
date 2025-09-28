class Solution:
    def rotateString(self, s: str, goal: str) -> bool: # n^2 time n space
        rotate_one = lambda s: s[-1] + s[:-1] # n time, n space
        
        n = len(s) # 1 time space
        current = s # 1 time space
        for i in s: # n iterations 
            if current == goal: # n time 1 space
                return True
            current = rotate_one(current) # n time space
        return False
