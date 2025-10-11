class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter
        if len(s) != len(goal):
            return False
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)
        count = len(diffs)
        if count == 0:
            if max(Counter(s).values()) > 1:
                return True
            return False
        if count == 2:
            return s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]
        return False
        
