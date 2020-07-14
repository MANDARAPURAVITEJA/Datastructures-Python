class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BisearchTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if(self.root is None):
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,temp):
        if(data<temp.data):
            if(temp.left is None):
                temp.left=Node(data)
            else:
                self._insert(data,temp.left)
        elif(data>temp.data):
            if(temp.right is None):
                temp.right=Node(data)
            else:
                self._insert(data,temp.right)
        else:
            print("Value is already present in tree")
    def find(self,data):
        if(self.root):
            isfound=self._find(data,self.root)
            if(isfound):
                return True
            return False
        else:
            return None
    def _find(self,data,temp):
        if(data>temp.data and temp.right):
            return self._find(data,temp.right)
        elif(data<temp.data and temp.left):
            return self._find(data,temp.left)
        if(data==temp.data):
            return True
def inOrder(root):
    #Write your code here
    if root is None:
        return              #left->root->right
    inOrder(root.left)
    print(root.data,end = " ")
    inOrder(root.right)
def preOrder(root):
    if root:
        print(root.data,end=" ")
        if root.left:               #root->left->right
            preOrder(root.left)
        if root.right:
            preOrder(root.right)
def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.data, end=' ')
def delete_Node(root, key):
  # if root doesn't exist, just return it
	if(root is None): 
		return root
	# Find the node in the left subtree	if key value is less than root value
	if root.data > key: 
		root.left = delete_Node(root.left, key)
	# Find the node in right subtree if key value is greater than root value, 
	elif root.data < key: 
		root.right= delete_Node(root.right, key)
	# Delete the node if root.value == key
	else: 
	# If there is no right children delete the node and new root would be root.left
		if not root.right:
			return root.left
	# If there is no left children delete the node and new root would be root.right	
		if not root.left:
			return root.right
  # If both left and right children exist in the node replace its value with 
  # the minmimum value in the right subtree. Now delete that minimum node
  # in the right subtree
		temp_val = root.right
		while temp_val.left:
			temp_val = temp_val.left
	# Replace value	
		root.data = temp_val.data       
  # Delete the minimum node in right subtree
		root.right = delete_Node(root.right,root.data)
	return root

b=BisearchTree()
b.insert(10)
b.insert(12)
b.insert(6)
b.insert(15)
b.insert(1)
b.insert(11)
b.insert(9)
b.insert(23)
#print(b.find(20))
inOrder(b.root);print("")
#preOrder(b.root);print("")
#postOrder(b.root)
delete_Node(b.root,10)
preOrder(b.root);print("")
#raviteja