# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        dummy.next = l1
        cur = dummy
        
        while l1 or l2:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            
            if cur.next:
                cur.next.val = sum
                cur = cur.next
            else:
                cur.next = l2
                cur.next.val = sum
                cur = cur.next
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                
        if carry:
            cur.next = ListNode(1, None)
            
        return dummy.next
