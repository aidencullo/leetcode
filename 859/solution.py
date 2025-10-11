class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter
        if Counter(s) != Counter(goal):
            return False
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] != goal[i]:
                count += 1
        if count == 2:
            return True
        if s == goal and max(Counter(s).values()) > 1:
            return True
        return False
        
