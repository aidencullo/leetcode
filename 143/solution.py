# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(node):
            if not node.next:
                return node
            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last

        def print_list(head):
            print("printing list now")
            while head:
                print(head.val)
                head = head.next

        reversed_head = reverse(head)
        print_list(reversed_head)
        
            
            
