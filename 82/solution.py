from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dups = set()

        runner = head

        while runner and runner.next:
            if runner.val == runner.next.val:
                dups.add(runner.val)
            runner = runner.next

        pre_head = ListNode(0, head)
        runner = pre_head

        while runner and runner.next:
            while runner.next and runner.next.val in dups:
                runner.next = runner.next.next
            runner = runner.next

        return pre_head.next
