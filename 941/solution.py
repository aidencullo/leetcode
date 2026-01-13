class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = max(arr)
        peak_idx = arr.index(peak)

        if peak_idx == 0 or peak_idx == len(arr) - 1:
            return False

        ascent = arr[:peak_idx + 1]
        descent = arr[peak_idx:]

        def is_unique(lst):
            return len(set(lst)) == len(lst)

        if not is_unique(descent):
            return False

        if not is_unique(ascent):
            return False

        def is_ascending(lst):
            prev = -math.inf
            for x in lst:
                if x <= prev:
                    return False
                prev = x
            return True

        def is_descending(lst):
            prev = math.inf
            for x in lst:
                if x >= prev:
                    return False
                prev = x
            return True

        if not is_ascending(ascent):
            return False

        if not is_descending(descent):
            return False

        return True
