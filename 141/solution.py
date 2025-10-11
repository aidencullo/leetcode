# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        skip_pointer = head
        while pointer and skip_pointer:
            pointer = pointer.next if pointer else None
            skip_pointer = skip_pointer.next if skip_pointer else None
            skip_pointer = skip_pointer.next if skip_pointer else None
            if pointer and skip_pointer and pointer == skip_pointer:
                return True
        return False
