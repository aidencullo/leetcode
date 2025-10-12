"""
LeetCode 605: Can Place Flowers

Time Complexity: O(n) where n is the length of the flowerbed
- We iterate through the flowerbed at most once
- Each iteration does constant time operations

Space Complexity: O(1) 
- We only use a constant amount of extra space (spaces counter, i pointer)
- The flowerbed modification creates a new list but this is typically not counted
- If we count the modified flowerbed: O(n) space

Approach:
- Add padding zeros to handle edge cases
- Iterate through flowerbed looking for three consecutive zeros
- When found, place a flower and skip the next position
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spaces = 0
        flowerbed  = [0] + flowerbed + [0]
        beds= len(flowerbed)
        i = 0
        while i < beds- 2:
            if flowerbed[i] != 0:
                i += 1
                continue
            if flowerbed[i + 1] != 0:
                i += 1
                continue
            if flowerbed[i + 2] != 0:
                i += 1
                continue
            spaces += 1
            i += 2
        return spaces >= n
