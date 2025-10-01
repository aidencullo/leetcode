def create_mat(n):
    return [[0 for j in range(n)] for i in range(n)]

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        class Matrix:
            def __init__(self, n):
                self.first_quadrant = create_mat(n)
                self.second_quadrant = create_mat(n)
                self.third_quadrant = create_mat(n)
                self.fourth_quadrant = create_mat(n)

        return False
