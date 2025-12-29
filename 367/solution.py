class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            k = l + (r - l) // 2

            if k ** 2 == num:
                return True
            elif k ** 2 < num:
                l = k + 1
            else:
                r = k - 1

        return False
