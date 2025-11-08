class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        min_diff_list = []
        n = len(arr)
        for i in range(n - 1):
            x = arr[i]
            y = arr[i + 1]
            diff = y - x
            if diff < min_diff:
                min_diff_list = [[x, y]]
                min_diff = diff
                continue
            if diff == min_diff:
                min_diff_list.append([x, y])
                continue
            
        return min_diff_list
