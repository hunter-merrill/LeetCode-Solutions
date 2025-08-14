# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Catch null lists
        match (list1, list2):
            case (None, None):
                return list1
            case (None, _):
                return list2
            case (_, None):
                return list1
        
        # Initialize head of combined list
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # Compare and relink to form a new list
        prev = head
        while list1 is not None or list2 is not None:
            match (list1, list2):
                case (None, _):
                    prev.next = list2
                    prev = list2
                    list2 = list2.next
                    continue
                case (_, None):
                    prev.next = list1
                    prev = list1
                    list1 = list1.next
                    continue
            
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        
        return head