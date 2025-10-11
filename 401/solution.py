from itertools import combinations, permutations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    res.append(f"{hour}:{minute:02}")
        return res
