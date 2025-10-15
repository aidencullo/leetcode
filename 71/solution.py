class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            if dir == '..' and stack:
                stack.pop()
            if dir != '..':
                stack.append(dir)
        return '/' + '/'.join(stack)
