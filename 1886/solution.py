def create_mat(n):
    return [[0 for j in range(n)] for i in range(n)]


class Matrix:
    def __init__(self, lst):
        self.n = len(lst)
        self.first_quadrant = create_mat(self.n)
        self.second_quadrant = create_mat(self.n)
        self.third_quadrant = create_mat(self.n)
        self.fourth_quadrant = create_mat(self.n)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return (
            self.first_quadrant == other.first_quadrant and
            self.second_quadrant == other.second_quadrant and
            self.third_quadrant == other.third_quadrant and
            self.fourth_quadrant == other.fourth_quadrant
        )

    def rotate(self):
        return self

    
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        start = Matrix(mat)
        final = Matrix(target)
        current = start

        for _ in range(4):
            current = current.rotate()
            if current == final:
                return True
        return False
