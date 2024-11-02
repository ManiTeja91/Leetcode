# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        num = val
        if head is None:
            return
        elif head.val == val:
            while head is not None and head.val == val:
                head = head.next
            if head == None:
                return
        prev = head
        temp = prev.next
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                temp.next = None
                temp = prev.next
            else:
                prev = prev.next
                temp = temp.next
        return head

            
        