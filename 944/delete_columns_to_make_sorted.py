class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        unsorted = 0
        
        for col in zip(*strs):
            if sorted(col) != list(col):
                unsorted += 1

        return unsorted
