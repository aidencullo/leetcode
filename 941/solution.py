class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = max(arr)
        peak_idx = arr.index(peak)

        if peak_idx == 0 or peak_idx == len(arr) - 1:
            return False

        before_max = arr[:peak_idx + 1]
        after_max = arr[peak_idx:]

        def is_ascending(lst):
            return all(a < b for a, b in zip(lst, lst[1:]))

        def is_descending(lst):
            return all(a > b for a, b in zip(lst, lst[1:]))

        if not is_ascending(before_max):
            return False

        if not is_descending(after_max):
            return False

        return True
