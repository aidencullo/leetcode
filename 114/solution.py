# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def traverse(node: Optional[TreeNode]) -> None:
            if node:
                left = node.left
                right = node.right
                rightmost_left = traverse(left)
                if left:
                    node.left = None
                    node.right = left
                    rightmost_left.right = right
                rightmost_right = traverse(right)
                if right:
                    return rightmost_right
                if left:
                    return rightmost_left
                return node

        traverse(root)
        return root
