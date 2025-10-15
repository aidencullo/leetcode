class Solution:
    def simplifyPath(self, path: str) -> str:

        def convert_double_periods(path):
            dirs = path.split('/')
            stack = []
            for dir in dirs:
                if dir == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(dir)
            return '/'.join(stack)

        def convert_forward_slashes(path):
            dirs = path.split('/')
            dirs_no_extra_forward_slashes = filter(None, dirs)
            return '/'.join(dirs_no_extra_forward_slashes)

        def convert_single_periods(path):
            dirs = path.split('/')
            dirs_without_periods = filter(lambda x: x != '.', dirs)
            return '/'.join(dirs_without_periods)
        
        single_period_path = convert_single_periods(path)
        without_slashes_path = convert_forward_slashes(single_period_path)
        canonical_path = convert_double_periods(without_slashes_path)
        return '/' + canonical_path
