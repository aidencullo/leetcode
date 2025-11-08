class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        from copy import deepcopy
        smoother = deepcopy(img)
        rows = len(img)
        cols = len(img[0])
        for row in range(len(img)):
            for col in range(len(img[0])):
                count = sum(1 for i in range(row - 1, row + 2) for j in range(col - 1, col + 2) if 0 <= i < rows and 0 <= j < cols)

                total = sum(
                    img[r][c]
                    for r in range(row-1, row+2)
                    for c in range(col-1, col+2)
                    if 0 <= r < rows and 0 <= c < cols
                )
                smoother[row][col] = total // count
        return smoother
