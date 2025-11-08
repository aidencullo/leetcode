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
            new_path = path + [node.val]
            if node and not node.left and not node.right:
                paths.append(new_path)
                return
            if node.left:
                follow_paths(node.left, new_path)
            if node.right:
                follow_paths(node.right, new_path)

        follow_paths(root, [])
        pretty_paths = ['->'.join([str(i) for i in path]) for path in paths]
        return pretty_paths
