class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def rotate_one(s):
            return s[-1] + s[:-1]
        
        n = len(s)
        current = s
        for i in s:
            if current == goal:
                return True
            current = rotate_one(current)
        return False
