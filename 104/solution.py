# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque

        q = deque()
        q.appendleft(root)

        d = 0

        while q:
            d += 1
            for i in range(len(q)):
                node = q.pop()

                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

        return d
