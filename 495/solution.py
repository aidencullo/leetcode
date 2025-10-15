class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_poisoned = 0
        import math
        end_of_poison = -math.inf
        n = len(timeSeries)
        for i, x in enumerate(timeSeries):
            if i == n - 1:
                time_poisoned += duration
                continue
            time_poisoned += min(duration, timeSeries[i + 1] - x)
        return time_poisoned
        
