class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_beauty = 0
        num_str = str(num)

        def sliding_substrings(s, size):
            for i in range(len(s) - size + 1):
                yield s[i : i + size]

        for x in sliding_substrings(num_str, k):
            x = int(x)
            if x == 0:
                continue
            if num % x == 0:
                k_beauty += 1

        return k_beauty
