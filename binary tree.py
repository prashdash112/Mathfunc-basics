class node:
    
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        
class bst:
    
    def __init__(self):
        
        self.root=None
        
    def insert(self,data):
        
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(data,self.root)
            
    def _insert(self,data,curr_node):
        
        if data<curr_node.data:
            if curr_node.left is None:
                curr_node.left=node(data)
            else:
                self._insert(data,curr_node.left)
                
        elif data>curr_node.data:
            if curr_node.right is None:
                curr_node.right=node(data)
            else:
                self._insert(data,curr_node.right)
        
        else:
            print('Value is already inserted in tree')
            
    def find(self,data):
        
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None
            
    def _find(self,data,curr_node):
    
        if data>curr_node.data and curr_node.right:
            return self._find(data,curr_node.right)
        elif data<curr_node.data and curr_node.left:
            return self._find(data,curr_node.left)
        if data==curr_node.data:
            return None
            
            
if __name__=='__main__':
    tree1=bst()
    tree1.insert(4)
    tree1.insert(2)
    tree1.insert(8)
    tree1.insert(5)
    tree1.insert(10)
    print(tree1.find(10))
