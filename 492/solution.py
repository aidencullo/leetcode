class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dimensions = None
        for w in range(1, area + 1):
            for l in range(w, area + 1):
                if w * l == area:
                    dimensions = [l, w]
        return dimensions
