#Remove duplicates from a sorted list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            l = [head.val]
            temp = head
            while temp.next:
                if temp.next.val in l:
                    temp.next = temp.next.next
                else:
                    l.append(temp.next.val)
                    temp = temp.next
        return head



