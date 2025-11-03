# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(last: ListNode, next: Optional[ListNode]) -> Optional[ListNode]:
            if not next:
                return last

            reverse_head = reverseList(next, next.next)

            next.next = last
            last.next = None

            return reverse_head

        return reverseList(head, head)
