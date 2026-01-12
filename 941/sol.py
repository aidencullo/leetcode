class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        # Climb up
        i = 0
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak can't be first or last
        if i == 0 or i == len(arr) - 1:
            return False
        
        # Climb down
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1
        
        return i == len(arr) - 1
