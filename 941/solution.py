class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # 1
            return False

        peak = max(arr) # n 
        peak_idx = arr.index(peak) # n

        if peak_idx == 0 or peak_idx == len(arr) - 1: # 1
            return False

        ascent = arr[:peak_idx + 1] # n
        descent = arr[peak_idx:] # n

        def is_unique(lst):
            return len(set(lst)) == len(lst) # n

        if not is_unique(descent): # n
            return False

        if not is_unique(ascent): # n
            return False

        if sorted(ascent) != ascent: # nlgn
            return False

        if sorted(descent, reverse=True) != descent: # nlgn
            return False

        return True
