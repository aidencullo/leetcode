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
                    return [node.val]
                res = []
                if node.left:
                    res.extend(helper(node.left))
                if node.right:
                    res.extend(helper(node.right))
                return res
            return helper(root)

        
        tree1_leaf_value_sequence = get_leaf_value_sequence(root1)
        tree2_leaf_value_sequence = get_leaf_value_sequence(root2)
        return tree1_leaf_value_sequence == tree2_leaf_value_sequence
