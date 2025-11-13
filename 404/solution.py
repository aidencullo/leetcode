# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return not node.left and not node.right
        
        def sumOfLeftLeaves(node):
            if not node:
                return
            
            if is_leaf(node):
                nonlocal left_leaves_sum
                left_leaves_sum += node.val
                return

            sumOfLeftLeaves(node.left)
            sumOfLeaves(node.right)

        def sumOfLeaves(node):
            if not node:
                return
            
            sumOfLeftLeaves(node.left)
            sumOfLeaves(node.right)


        left_leaves_sum = 0
        sumOfLeaves(root)
        return left_leaves_sum
