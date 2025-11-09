class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1

        while l <= r:
            k = (l + r) // 2
            el = letters[k]

            if el <= target:
                l = k + 1
            else:
                r = k - 1

        if l >= n:
            return letters[0]
        return letters[l]
        

