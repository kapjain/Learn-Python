# A Python class that represents an individual node 
# in a Binary Tree https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
class Node: 
    def __init__(self, value): 
        self.left = None
        self.right = None
        self.value = value 

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:             
                self._insert(value, curr_node.left)
        elif value > curr_node.value:
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:             
                self._insert(value, curr_node.right)
        else:
            print("Duplicate entry not allowed in BST")

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None
    
    # Python program to find the node with minimum value in BST 
    def findMinVal(self):
        minnode = self.findMinValNode(self.root)
        return minnode.value
        
    def findMinValNode(self, node):
        current = node 
        """ Given a non-empty binary search tree,   
        return the minimum data value found in that  
        tree. Note that the entire tree does not need  
        to be searched. """        
    
        if current is not None:
            # loop down to find the leftmost leaf 
            while(current.left is not None): 
                current = current.left 
    
        return current
    
    def delete(self, value):
        if self.root == None:
            return self.root
        else:
            return self._delete(self.root,value)
    
    # Given a binary search tree and a key, this function 
    # delete the key and returns the new root 
    def _delete(self,root, value): 
    
        # Base Case 
        if root is None: 
            return root 
    
        # If the key to be deleted is smaller than the root's 
        # key then it lies in left subtree 
        if value < root.value: 
            root.left = self._delete(root.left, value) 
    
        # If the kye to be delete is greater than the root's key 
        # then it lies in right subtree 
        elif(value > root.value): 
            root.right = self._delete(root.right, value) 
    
        # If key is same as root's key, then this is the node 
        # to be deleted 
        else: 
            
            # Case 1: Node with no child
            if root.left == None and root.right == None:
                root = None
                return root 
            # Case 2: Node with only one child
            elif root.left is None : 
                temp = root.right 
                root = None
                return temp 
                
            elif root.right is None : 
                temp = root.left 
                root = None
                return temp 
    
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = self.findMinValNode(root.right) 
    
            # Copy the inorder successor's content to this node 
            root.value = temp.value 
    
            # Delete the inorder successor 
            root.right = self._delete(root.right , temp.value) 
    
    
        return root 

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print (str(node.value) + ' ')
            self._printTree(node.right)

    def count(self):
        count = 0
        if(self.root != None):
            count =  self._count(self.root,count)
        return count
    
    def _count(self, node, count):
        if(node != None):
            count = self._count(node.left, count)
            count += 1
            count = self._count(node.right, count)
        return count

    def inorder(self):
        if(self.root != None):
            self._inorder(self.root)

    def _inorder(self, node):
        if(node != None):
            self._inorder(node.left)
            print (str(node.value) + ' ')
            self._inorder(node.right)
            
    def preorder(self):
        if(self.root != None):
            self._preorder(self.root)

    def _preorder(self, node):
        if(node != None):
            print (str(node.value) + ' ')
            self._preorder(node.left)
            self._preorder(node.right)            
            
    def postorder(self):
        if(self.root != None):
            self._postorder(self.root)

    def _postorder(self, node):
        if(node != None):
            self._postorder(node.left)
            self._postorder(node.right)
            print (str(node.value) + ' ') 
            
    def find(self, value):
        if(self.root != None):
            return self._find(value, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.value):
            return node.value
        elif(val < node.value and node.left != None):
            return self._find(val, node.left)
        elif(val > node.value and node.right != None):
            return self._find(val, node.right)
        return None
    

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left,cur_height+1)
        right_height=self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)
# Driver program to test above functions 
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  
obj = BinaryTree()
obj.insert(50)
obj.insert(30)
obj.insert(20)
obj.insert(40)
obj.insert(70)
obj.insert(60) 
obj.insert(80) 

print("height of the tree %s"%obj.height())
print("Minimun value in the tree %s"%obj.findMinVal())
if obj.find(90):
    print("found it")
else:
    print("did not find it")
print("Total number of childs : %s"%(obj.count()))
print ("Inorder traversal of the given tree")
obj.inorder() 
  
print ("\nDelete 20")
root = obj.delete(20)
print ("Inorder traversal of the modified tree")
obj.inorder() 
print("Total number of childs : %s"%(obj.count()))

print ("\nDelete 30")
root = obj.delete(30)
print ("Inorder traversal of the modified tree")
obj.inorder()
print("Total number of childs : %s"%(obj.count()))

print ("\nDelete 50")
root = obj.delete(50)
print ("Inorder traversal of the modified tree")
obj.inorder()