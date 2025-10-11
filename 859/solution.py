class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                new_s = list(s)
                new_s[i], new_s[j] = new_s[j], new_s[i]
                new_s = "".join(new_s)
                if new_s == goal:
                    return True
        return False
