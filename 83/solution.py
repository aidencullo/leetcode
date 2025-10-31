# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        runner = head
        while runner:
            seen.add(runner.val)
            while runner.next and runner.next.val in seen:
                runner.next = runner.next.next
            runner = runner.next
        return head
        
