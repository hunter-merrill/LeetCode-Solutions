import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Naive: traverse the whole list, tallying the # of elements
# --> re-traverse from head up to numElements/2, return that node
# 
# Little better:
# Store list in an array as you go, return arr[n//2]

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0

        node = head
        while node.next:
            length += 1
            node = node.next

        node = head
        for i in range(length // 2):
            node = node.next
        if (length % 2 == 1):
            node = node.next

        return node