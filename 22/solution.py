class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(open_n, close_n, running):
            if open_n == close_n == 0:
                parentheses.append(running)
                return

            if open_n > 0:
                gen(open_n - 1, close_n, running + '(')
            if open_n < close_n:
                gen(open_n, close_n - 1, running + ')')
        
        parentheses = []
        gen(n, n, "")
        return parentheses
