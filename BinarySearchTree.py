class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.data == key:
			return root
		elif root.data < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=' ')
		inorder(root.right)

def search(root, key):
	if root is None or root.data == key:
		return root
	if root.data < key :
		return search(root.right, key)
	if root.data > key :
		return search(root.left, key)

def minNodeValue(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    if root == None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    if key > root.data :
        root.right = deleteNode(root.right, key)

    if key == root.data :
        if root.left == None:
            temp = root.right
            root = None
            return temp
 
        if root.right == None:
            temp = root.left
            root = None
            return temp
 
        temp = minNodeValue(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

ch=-1
root = None
while True :
	ch = int(input("\nAvailable Operations :\n1. Inorder Traversal\n2. Insert\n3. Delete\n4. Search\n5. Exit\nEnter your choice : "))
	if ch==1 :
		if root == None :
			print("BST in empty")
		else:
			print(f"Root : {root.data}")
			inorder(root)
	elif ch==2 :
		val = int(input("Enter an integer : "))
		root = insert(root, val)
		print(f"Updated BST : Rooted at {root.data}")
		inorder(root)
	elif ch==3 :
		val = int(input("Enter an item for deletion : "))
		root = deleteNode(root, val)
		if root :
			print(f"Updated BST : Rooted at {root.data}")
			inorder(root)
	elif ch==4 :
		val = int(input("Enter an item for Search : "))
		temp = search(root, val)
		if temp == None :
			print(f"{val} is not present in BST")
		else :
			print(f"{val} is present in BST")
	elif ch==5 :
		import sys
		sys.exit()
	else :
		print("Enter a valid choice")

# Driver program to test the above functions
# Let us create the following BST
# 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)