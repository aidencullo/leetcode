class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_brackets = set('([{')
        right_brackets_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in left_brackets:
                stack.append(c)
            elif not stack:
                return False
            elif stack.pop() != right_brackets_dict[c]:
                return False
        return not stack

    
