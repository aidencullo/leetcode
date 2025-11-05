class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        res = []
        for char in s:
            if char.isalpha():
                stack.append(char)
        for char in s:
            if char.isalpha():
                res.append(stack.pop())
            else:
                res.append(char)
        return ''.join(res)
