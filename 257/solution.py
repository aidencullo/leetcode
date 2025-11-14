# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return
        
        def is_leaf(node):
            return not node.left and not node.right

        paths = []
        path = []
        
        def dfs(node):

            path.append(node.val)
            
            if is_leaf(node):
                paths.append(path.copy())
                path.pop()
                return

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            path.pop()
            

        dfs(root)
        return ['->'.join(str(node) for node in path) for path in paths]
