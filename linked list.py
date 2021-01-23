class node: # defining class node for creating several nodes 
    
    def __init__(self,data): # Function to initialise the node object 
        
        self.data=data; 
        self.next=None

# Linked List class contains a Node object 
class linkedlist:       # defining class linkedlist for assigning the head of linkedlist to a node 
    
    def __init__(self): # Function to initialize head 
        
        self.head=None
        
if __name__=='__main__':
    
    lst=linkedlist() #  linkedlist object creation 
    
    lst.head=node(1) 
    
    nxt2=node(10)
    
    nxt3=node(100)
    
    lst.head.next=nxt2 # defining relation between different nodes
    
    nxt2.next=nxt3
