# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        seen = set()
        duplicate = set()

        cur = head
        while cur:
            if cur.val in seen:
                duplicate.add(cur.val)
            seen.add(cur.val)
            cur = cur.next

        new_head = ListNode(-101, head)
        cur = new_head
        while cur and cur.next:
            if cur.next.val in duplicate:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return new_head.next
