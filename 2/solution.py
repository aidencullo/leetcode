# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getLen(linked_list):
            ptr = linked_list
            total = 0
            while ptr:
                total += 1
                ptr = ptr.next
            return total
        
        def LlToNumber(linked_list):
            n = getLen(linked_list):
            head = linked_list
            total = 0
            for i in range(n - 1, -1, -1):
                total += head.val
                head = head.next
            return total
        
        x1 = LlToNumber(l1)
        x2 = LlToNumber(l2)
        x3 = x1 + x2
        l3 = NumberToLl(x3)
        return l3
