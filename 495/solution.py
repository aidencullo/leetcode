import math
import itertools

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_poisoned = 0
        end_of_poison = -math.inf
        n = len(timeSeries)
        for i, x in enumerate(itertools.islice(timeSeries, 0, n - 1)):
            time_poisoned += min(duration, timeSeries[i + 1] - x)
        time_poisoned += duration
        return time_poisoned
        
