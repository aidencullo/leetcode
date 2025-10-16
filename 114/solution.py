# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def traverse(root: Optional[TreeNode]) -> None:
            if root:
                left = traverse(root.left)
                left.right = root.right
                traverse(root.right)
                root.right = root.left
        traverse(root)
        return root
