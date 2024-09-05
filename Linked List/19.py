class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def printlinkedlist(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ----> ",end="")
                temp = temp.next
            print("End")
    
    def reverselist(self):
        curr = self.head
        prev = None
        while curr is not None:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        self.head = prev
    
                     
    def removeNthFromEnd(self, n):
        #find length
        l = 0
        temp = self.head
        while temp:
            l += 1
            temp =  temp.next
        #remove the head if l == 1
        if l == 1:
            self.head = None
        elif l == 2:
            if n == 2:
                self.head = self.head.next
            elif n == 1:
                self.head.next = None
        else:
            self.reverselist()
            if n == 1:
                self.head = self.head.next
            else:
                ptr = 1
                temp = self.head
                while ptr < n-1:
                    ptr += 1
                    temp = temp.next
                temp.next = temp.next.next
            self.reverselist()
            
                
       
            
    

if __name__ == "__main__":
    l = LL()  
    l.insert_at_begin(3)  
    l.insert_at_begin(2)
    l.insert_at_begin(1)
    
    print("Before removing")
    l.printlinkedlist()
    l.removeNthFromEnd(1)
    print("After removing")
    l.printlinkedlist()
    
#we need to reverse once remove ther element and reverse again