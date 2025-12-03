# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        leaves_sum = 0
        q = deque()
        q.append(root)
        last_q = deque()

        while q:

            new_q = deque()
            last_q = q

            while q:
                node = q.popleft()
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                

            q = new_q


        return sum(last_q)
