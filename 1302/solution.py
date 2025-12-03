# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)

        while q:

            new_q = deque()
            leaves_sum = 0

            while q:
                node = q.popleft()
                leaves_sum += node.val
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                
            q = new_q


        return leaves_sum
