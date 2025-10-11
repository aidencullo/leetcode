from itertools import combinations, permutations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for i in range(turnedOn + 1):
            minutes = self.readMinutes(i)
            hours = self.readHours(turnedOn - i)
            if minutes and hours:
                for minute in minutes:
                    for hour in hours:
                        times.append(hour + ":" + minute.zfill(2))
        return times
        
    def readHours(self, turnedOn: int) -> List[str]:
        hours = [1, 2, 4, 8]
        res = []
        for c in combinations(hours, turnedOn):
            total = sum(c)
            if total < 12:
                res.append(str(total))
        return res

    def readMinutes(self, turnedOn: int) -> List[str]:
        minutes = [1, 2, 4, 8, 16, 32]
        res = []
        for c in combinations(minutes, turnedOn):
            total = sum(c)
            if total < 60:
                res.append(str(total))
        return res
