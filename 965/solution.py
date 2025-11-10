# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(node, x):
            if not node:
                return True
            
            return node.val == x and helper(node.left, x) and helper(node.right, x)

        c = root.val
        return helper(root, c)
