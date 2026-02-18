class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(goal)

        if c1 != c2:
            return False

        differences = sum(1 for a, b in zip(s, goal) if a != b)

        if differences > 2:
            return False

        max_occurrences = max(c1.values())

        if differences == 0 and max_occurrences < 2:
            return False

        return True

        
