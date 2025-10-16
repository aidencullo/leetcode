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
                nodes.append(root)
                traverse(root.left)
                traverse(root.right)

        nodes = []
        traverse(root)
        head = TreeNode(0)
        current = head
        for node in nodes:
            current.right = node
            current = node
            current.left = None
            current.right = None
        return head.right
                
