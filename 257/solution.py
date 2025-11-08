# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def follow_paths(node, path):
            if not node:
                paths.append(path)
                return
            path.append(node.val)
            follow_paths(node.left, path)
            follow_paths(node.right, path)

        follow_paths(root, [])
        return paths
