# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(path + [node.val])
                return

            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])

        dfs(root, [])

        return ['->'.join(str(x) for x in path) for path in res]
