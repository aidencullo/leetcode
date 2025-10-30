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
        while not (l1 is None and l2 is None):
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            result += digit % 10 * magnitude
            digit //= 10
            magnitude *= 10
        result += digit % 10 * magnitude
        if not result:
            return ListNode()
        result_linked_list = ListNode()
        runner = result_linked_list
        while result:
            current = ListNode(result % 10)
            runner.next = current
            runner = runner.next
            result //= 10
        return result_linked_list.next
                
