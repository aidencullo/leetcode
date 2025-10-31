# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def measure(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        a = measure(headA)
        b = measure(headB)

        if a > b:
            for _ in range(a - b):
                headA = headA.next
        else:
            for _ in range(b - a):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
            
