# insertion in head of a linked list

class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    
    def __init__(self):
        self.head=None
        
    def print_lst(self):
        printval = self.head
        
        while printval is not None:
            print (printval.data)
            printval = printval.next
            
    def atbegin(self,val):
        newnode=node(val)
        
# Update the new nodes next val to existing node
        newnode.next = self.head
        self.head = newnode
        
        
if __name__=='__main__':

    lst = linkedlist()
    
    lst.head = node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    lst.head.next = e2
    e2.nextval = e3

    lst.atbegin("Sun")

    lst.print_lst()
