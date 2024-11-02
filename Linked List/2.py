#Add 2 numbers stored in reverse order in a linked list and return the reverse order in linked list
#0ms , beats 100% 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0

            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10

            node = ListNode(sum_val%10)
            curr.next = node
            curr = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            

        return dummy.next

