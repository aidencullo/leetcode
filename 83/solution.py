# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        while runner:
            while runner.next and runner.val == runner.next.val:
                runner.next = runner.next.next
            runner = runner.next
        return head
        
