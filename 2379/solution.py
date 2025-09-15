class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Time Complexity: O(n) where n is the length of blocks
        # Space Complexity: O(1) - only using a constant amount of extra space
        white = 0
        min_white = k
        l, r = 0, k - 1
        n = len(blocks)
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        l += 1
        r += 1
        min_white = min(min_white, white)
        while r < n:      
            if blocks[r] == 'W':
                white += 1
            if blocks[l - 1] == 'W':
                white -= 1
            min_white = min(min_white, white)
            l += 1
            r += 1     
        return min_white