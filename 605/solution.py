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
