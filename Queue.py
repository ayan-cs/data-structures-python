# QUEUE
class Node:
    def __init__(self, data):
        self.data=data
        self.link=None

def printQueue(head) :
    print("Print Queue")
    if head == None:
        print("Queue is empty")
    else:
        while head != None:
            print(head,' ',head.data,' ',head.link)
            head = head.link

def enQueue(head, rear, data):
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
    print("Elements added successfully")
    return (head, rear)

def deQueue(head, rear):
    if head == None:
        print("Queue is empty")
    else:
        head = head.link
        if head == None:
            rear = None
    return (head, rear)

def searchQueue(head, elem):
    if head==None:
        print("Queue is empty")
    else:
        loc=[]
        i=1
        while head != None:
            if head.data == elem:
                loc.append(i)
            i+=1
            head = head.link
        if len(loc)==0:
            print("Element not found")
        else:
            print(f"Element found at positions : {loc}")

ch = -1
head = None
rear = None
while(True):
    ch = int(input("\nAvailable Operations\n1. Print LL\n2. Add Node\n3. Delete Node\n4. Search by element\n5. Exit\nEnter your choice : "))
    if ch==1:
        printQueue(head)
    elif ch==2:
        data = input("Enter data in one line, space seperated : ")
        head, rear = enQueue(head, rear, data)
    elif ch==3:
        head, rear = deQueue(head, rear)
    elif ch==4 :
        n = input("Enter value to search : ")
        searchQueue(head, n)
    elif ch==5 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
