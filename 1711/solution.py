class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        good_meals = 0
        n = len(deliciousness)
        
        for i in range(n):
            x = deliciousness[i]
            for j in range(i + 1, n):
                if x + y == 0:
                    continue
                y = deliciousness[j]
                p = math.log2(x + y)
                if int(p) == p:
                    good_meals += 1

        return good_meals % (10 ** 9 + 7)
