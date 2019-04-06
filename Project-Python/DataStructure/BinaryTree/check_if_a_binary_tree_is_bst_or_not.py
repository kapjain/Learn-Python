# Python program to check if a binary tree is bst or not 
"""
METHOD 1 (Correct but not efficient)
For each node, check if max value in left subtree is smaller than the node and min value in right subtree greater than the node.

/* Returns true if a binary tree is a binary search tree */
int isBST(struct node* node) 
{ 
if (node == NULL) 
    return(true); 
    
/* false if the max of the left is > than us */
if (node->left!=NULL && maxValue(node->left) > node->data) 
    return(false); 
    
/* false if the min of the right is <= than us */
if (node->right!=NULL && minValue(node->right) < node->data) 
    return(false); 
    
/* false if, recursively, the left or right is not a BST */
if (!isBST(node->left) || !isBST(node->right)) 
    return(false); 
    
/* passing all that, it's a BST */
return(true); 
} 
METHOD 3 (Correct and Efficient)
Method 1 above runs slowly since it traverses over some parts of the tree many times. A better solution looks at each node only
 once. The trick is to write a utility helper function isBSTUtil(struct node* node, int min, int max) that traverses down the 
 tree keeping track of the narrowing min and max allowed values as it goes, looking at each node only once. The initial values
  for min and max should be INT_MIN and INT_MAX  they narrow from there

"""
INT_MAX = 4294967296
INT_MIN = -4294967296

# A binary tree node 
class Node: 

    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree 
# (efficient version) 
def isBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 

# Retusn true if the given tree is a BST and its values 
# >= min and <= max 
def isBSTUtil(node, mini, maxi): 
    
    # An empty tree is BST 
    if node is None: 
        return True

    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False

    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBSTUtil(node.left, mini, node.data -1) and
        isBSTUtil(node.right, node.data+1, maxi)) 

# Driver program to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 

if (isBST(root)): 
    print ("Is BST")
else: 
    print ("Not a BST")
