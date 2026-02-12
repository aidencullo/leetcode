# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/
#
# Given a string s, return the string after replacing every uppercase letter
# with the corresponding lowercase letter.

class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s:
            if 'A' <= c <= 'Z':
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)
        return ''.join(result)
