# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        magnitude = 1
        digit = 0
        result = ListNode()
        runner = result
        while not (l1 is None and l2 is None):
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            digit, val = divmod(digit, 10)
            cur = ListNode(val)
            runner.next = cur
            runner = runner.next
        digit, val = divmod(digit, 10)
        if val:
            cur = ListNode(val)
            runner.next = cur
        return result.next
                
