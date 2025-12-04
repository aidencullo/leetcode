# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def recover(root):
            def recover_recurse(node):
                if not node:
                    return
                
                x = node.val
                
                if node.left:
                    node.left.val = 2 * x + 1
                    self.values.add(node.left.val)

                if node.right:
                    node.right.val = 2 * x + 2
                    self.values.add(node.right.val)

                recover_recurse(node.right)
                recover_recurse(node.left)
                
            root.val = 0
            recover_recurse(root)
        
        self.root = root
        self.values = set((0,))
        recover(self.root)

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
