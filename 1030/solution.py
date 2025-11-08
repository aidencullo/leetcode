class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        d = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                distance = abs(row - rCenter) + abs(col - cCenter)
                d[distance].append([row, col])


        cells = []
        for distance in sorted(d):
            cells.extend(d[distance])
        return cells
