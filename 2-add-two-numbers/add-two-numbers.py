# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def readByDigits(l: ListNode) -> int:
            num = 0
            place = 1

            while l:
                num += l.val * place
                place *= 10
                l = l.next

            return num
        
        def intToDigits(num: int) -> ListNode:
            l = ListNode(val=num % 10)
            head = l
            place = 10

            while num >= place:
                l.next = ListNode()
                l = l.next
                
                remainder = num % (10 * place)
                l.val = remainder // place
                place *= 10
            
            return head

        num1 = readByDigits(l1)
        num2 = readByDigits(l2)
        return intToDigits(num1 + num2)