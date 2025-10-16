class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        prev, stack = None, [root]
        while stack:
            node = stack.pop()

            if prev:
                prev.left, prev.right = None, node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node
            
        return root
