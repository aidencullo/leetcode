class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        rows = [row1, row2, row3]

        ans = []

        for word in words:
            word_lowered = word.lower()
            word_row = None

            for row in rows:
                if word_lowered[0] in row:
                    word_row = row
                    break

            if word_row is None:
                continue

            for c in word_lowered:
                if c not in word_row:
                    break
            else:
                ans.append(word)

        return ans
