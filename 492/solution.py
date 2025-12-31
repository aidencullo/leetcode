class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dimensions = None
        for width in range(1, area + 1):
            if area // width != area / width:
                continue

            length = area // width
            
            left, right = width, area
            while left <= right:
                k = (left + right) // 2

                if length >= k:
                    r = k + 1
                else:
                    l = k - 1

            if right < width:
                continue

            if right == length:
                dimensions = [length, width]
                    
        return dimensions
