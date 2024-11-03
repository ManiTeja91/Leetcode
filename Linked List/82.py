# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head   

        curr = head
        arr1 = []
        arr2  = []
        num = -500000
        while curr:
            i = curr.val 
            if i != num:
                arr1.append(i)
            elif i == num:
                arr2.append(i)
                if i in arr1:
                    arr1.remove(i)
            num = i
            curr = curr.next

        if len(arr1) == 0:
            return None

        res_head = ListNode(arr1[0])
        curr = res_head
        for i in range(1, len(arr1)):
            node = ListNode(arr1[i])
            curr.next = node
            curr = curr.next    
        return res_head 

    
#Oms 100%

        



        
        