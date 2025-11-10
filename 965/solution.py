# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            while node:
                if node.val != root.val:
                    return False
                if node.right:
                    stack.append(node.right)
                node = node.left

        return True


#     # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         stack = [root]
#         values = []

#         while stack:
#             node = stack.pop()
#             while node:
#                 values.append(node.val)
#                 if node.right:
#                     stack.append(node.right)
#                 node = node.left

#         return sum(x for x in values if low <= x <= high)

        
