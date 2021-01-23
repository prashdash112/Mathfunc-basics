# linked list traversal

class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    
    def __init__(self):
        self.head=None
        
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main__':

    lst=linkedlist()
    lst.head=node(1)
    nxt2=node(10)
    nxt3=node(100)
    lst.head.next=nxt2
    nxt2.next=nxt3
    lst.print_list()
