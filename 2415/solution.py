# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        level = 0

        while q:

            qlen = len(q)
            stack = []
            node_queue = deque()
            for _ in range(qlen):
                node = q.popleft()
                stack.append(node.val)
                node_queue.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                while node_queue:
                    node = node_queue.popleft()
                    node.val = stack.pop()

            level += 1

        return root
