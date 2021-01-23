# linked list traversal

class node: # defining class node for creating several nodes 
    
    def __init__(self,data): # Function to initialise the node object 
        self.data=data
        self.next=None
        
class linkedlist: # Linked List class contains a Node object 
    
    def __init__(self): # Function to initialize head 
        self.head=None
        
    def print_list(self): #method definition for traversal of elements 
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main__':

    lst=linkedlist() #  linkedlist object creation 
    lst.head=node(1)
    nxt2=node(10)
    nxt3=node(100)
    lst.head.next=nxt2 # defining relation between different nodes
    nxt2.next=nxt3
    lst.print_list() # prints the elements of the linked list
