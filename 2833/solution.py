class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int: 
        left = moves.count('L') 
        right = moves.count('R')
        underscore = moves.count('_')
        return max(left, right) - min(left, right) + underscore
