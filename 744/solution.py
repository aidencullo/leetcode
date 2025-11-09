class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = bisect.bisect_right(letters, target)


        if l >= n:
            return letters[0]
        return letters[l]
        

