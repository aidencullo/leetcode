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
        def sum_beds(start, end):
            beds = 0
            if start < 0:
                start += 1
            if end == len(flowerbed):
                end -= 1

            for i in range(start, end + 1):
                beds += flowerbed[i]

            return beds
        
        spaces = 0
        flowerbed  = flowerbed
        num_flowerbeds = len(flowerbed)
        i = 0
        while i < num_flowerbeds:
            if sum_beds(i - 1, i + 1) != 0:
                i += 1
            else:
                spaces += 1
                i += 2
        return spaces >= n
