# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        currNode = head
        prevNode = nextNode = None
        while currNode:
            nextNode = currNode.next # Store current node's 'next' pointer
            currNode.next = prevNode # Point current node toward previous node
            prevNode = currNode # Store current node so next node can point to it
            currNode = nextNode

        return prevNode