# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_value_sequence(root):
            def helper(node):
                if not node.left and not node.right:
                    sequence.append(node.val)
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)
            sequence = []
            helper(root)
            return sequence

        
        tree1_leaf_value_sequence = get_leaf_value_sequence(root1)
        tree2_leaf_value_sequence = get_leaf_value_sequence(root2)
        return tree1_leaf_value_sequence == tree2_leaf_value_sequence
