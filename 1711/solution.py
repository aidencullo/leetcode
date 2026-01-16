class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        def is_pow(z):
            lg = math.log2(z)
            return int(lg) == lg
        
        good_meals = 0
        counter = Counter(deliciousness)
        unique_deliciousness = set(deliciousness)
        
        for i, x in enumerate(unique_deliciousness):
            for y in islice(unique_deliciousness, i + 1, None):
                if is_pow(x + y):
                    good_meals += counter[x] * counter[y]

        for x in unique_deliciousness:
            cnt = counter[x]
            if cnt > 1 and is_pow(2 * x):
                good_meals += math.comb(cnt, 2)

        return good_meals % (10 ** 9 + 7)
