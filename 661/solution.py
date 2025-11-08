class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        smoother = [[0] * cols for row in range(rows)]
        for row in range(len(img)):
            for col in range(len(img[0])):
                count = 0
                total = 0
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if 0 <= i < rows and 0 <= j < cols:
                            total += img[i][j]
                            count += 1
                smoother[row][col] = total // count
        return smoother
