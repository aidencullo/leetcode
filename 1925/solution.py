class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                triple = x ** 2 + y ** 2
                triple_sqrt = math.sqrt(x ** 2 + y ** 2)
                if int(triple_sqrt) == triple_sqrt and triple_sqrt <= n:
                        count += 1
        return count
                    
