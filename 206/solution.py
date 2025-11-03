# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
        reversed_head = ListNode()
        runner = reversed_head
        while val := stack.pop():
            cur = ListNode(val)
            runner.next = cur
            runner = runner.next
        return reversed_head.next
