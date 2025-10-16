# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = []
        if root:
            stack.append(root)
        head = TreeNode(0)
        last = head

        while stack:
            node = stack.pop()
            last.left = None
            last.right = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            last = node
            
        return root
