"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None:None}

        #Maping original nodes with duplicate nodes in dict
        curr = head
        while curr:
            node = Node(curr.val)
            copies[curr] = node
            curr = curr.next
        
        #Creating new linkedlist with nodes in dictionary
        curr = head
        while curr:
            copy = copies[curr]
            copy.next = copies[curr.next]
            copy.random = copies[curr.random]
            curr = curr.next
        return copies[head]



        #27 MS 97.67%