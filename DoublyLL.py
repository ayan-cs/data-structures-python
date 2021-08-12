# DOUBLY LINKED LIST

class Node :
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def printLL(head):
    print("Print LL")
    if head == None:
        print("LL is empty")
    else:
        while head != None:
            print(head.left,' ',head.data,' ',head.right)
            head = head.right

def insertNode(head, data):
    data = data.split()
    if head==None:
        elem = data[0]
        head = Node(elem)
        data.remove(elem)
    temp=head
    while temp.right != None:
        temp = temp.right
    for i in data:
        nn = Node(i)
        nn.left = temp
        temp.right = nn
        temp = temp.right
    print("Data added successfully")
    return head

def deleteNode(head, data):
    flag=0
    if head.data == data:
        head = head.right
        if head != None :
            head.left = None
        flag=1
    else :
        prev = head
        temp = head.right
        while temp != None:
            if temp.data == data and temp.right == None:
                prev.right = None
                flag=1
                break
            elif temp.data == data and temp.right != None :
                prev.right = temp.right
                temp.right.left = prev
                flag=1
                break
            else :
                prev = temp
                temp = temp.right
    if flag==1:
        print("Element deleted successfully")
    else:
        print("Element couldn't be found")
    return head

def searchLL(head, elem):
    if head==None:
        print("LL is empty")
    else:
        loc=[]
        i=1
        while head != None:
            if head.data == elem:
                loc.append(i)
            i+=1
            head = head.right
        if len(loc)==0:
            print("Element not found")
        else:
            print(f"Element found at positions : {loc}")

ch = -1
head = None
while(True):
    ch = int(input("\nAvailable Operations\n1. Print LL\n2. Add Node\n3. Delete Node by value\n4. Search by element\n5. Exit\nEnter your choice : "))
    if ch==1:
        printLL(head)
    elif ch==2:
        data = input("Enter data in one line, space seperated : ")
        head = insertNode(head, data)
    elif ch==3:
        if head == None:
            print("LL is empty")
        else:
            n = input("Enter the Value you want to delete : ")
            head = deleteNode(head, n)
    elif ch==4 :
        n = input("Enter value to search : ")
        searchLL(head, n)
    elif ch==5 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
