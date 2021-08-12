# CIRCULAR LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

def printLL(head, rear) :
    print("Print LL")
    if head == None:
        print("LL is empty")
    else:
        while head != rear:
            print(head,' ',head.data,' ',head.link)
            head = head.link
        print(head,' ',head.data,' ',head.link)

def insertNode(head, rear, data):
    data = data.split()
    if rear == None:
        elem = data[0]
        rear = Node(elem)
        data.remove(elem)
        head = rear
    for i in data:
        nn = Node(i)
        rear.link = nn
        rear = nn
    rear.link = head
    print("Elements added successfully")
    return (head, rear)

def deleteNode(head, rear, data):
    flag=0
    if head.data == data:
        if head == rear :
            head = None
            rear = None
        else:
            head = head.link
            rear.link = head
        flag=1
    else :
        prev = head
        temp = head.link
        while temp != rear:
            if temp.data == data:
                prev.link = temp.link
                flag=1
                break
            else :
                prev = temp
                temp = temp.link
        if temp.data == data:
            rear = prev
            rear.link = head
            flag=1
    if flag==1:
        print("Element deleted successfully")
    else:
        print("Element couldn't be found")
    return (head, rear)

def searchLL(head, rear, elem):
    if head==None:
        print("LL is empty")
    else:
        loc=[]
        i=1
        while head != rear:
            if head.data == elem:
                loc.append(i)
            i+=1
            head = head.link
        if head.data == elem:
            loc.append(i)
    if len(loc)==0:
        print("Element not found")
    else:
        print(f"Element found at positions : {loc}")

ch = -1
head = None
rear = None
while(True):
    ch = int(input("\nAvailable Operations\n1. Print LL\n2. Add Node\n3. Delete Node by value\n4. Search by element\n5. Exit\nEnter your choice : "))
    if ch==1:
        printLL(head, rear)
    elif ch==2:
        data = input("Enter data in one line, space seperated : ")
        head, rear = insertNode(head, rear, data)
    elif ch==3: 
        if head == None :
            print("LL is empty")
        else:
            n = input("Enter the Value you want to delete : ")
            head, rear = deleteNode(head, rear, n)
    elif ch==4 :
        if head == None :
            print("LL is empty")
        else:
            n = input("Enter value to search : ")
            searchLL(head, rear, n)
    elif ch==5 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
