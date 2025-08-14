# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize head node
        head = ListNode()
        prev = head

        # Compare and relink to form a new list
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        
        prev.next = list1 or list2 # Migrate null check to the end!!! new syntax I learned :o
        
        # Return list, skipping dummy head
        return head.next