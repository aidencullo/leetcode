class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        def is_pow(z):
            return math.log2(z) ** 2 == z
        
        good_meals = 0
        counter = Counter(deliciousness)
        unique_deliciousness = set(deliciousness)
        
        for i, x in enumerate(unique_deliciousness):
            for y in islice(unique_deliciousness, i + 1, None):
                if is_pow(x + y):
                    good_meals += counter[x] * counter[y]

        return good_meals % (10 ** 9 + 7)
