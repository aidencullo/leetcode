# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        runner = result

        while list1 or list2:
            if list1 and (not list2 or list1.val < list2.val):
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next
            runner = runner.next

        if list1:
            runner.next = list1
        else:
            runner.next = list2

        return result.next
            
