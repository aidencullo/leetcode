# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            runner = headB
            while runner:
                if headA is runner:
                    return runner
                runner = runner.next
            headA = headA.next
        
