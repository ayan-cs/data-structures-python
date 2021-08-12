# DE-QUEUE

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

def rear_enQueue(head, rear, data):
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
    print("Elements added at the Rear end successfully")
    return (head, rear)

def front_enQueue(head, rear, data):
    data = data.split()
    data.reverse()
    if head == None:
        elem = data[0]
        rear = Node(elem)
        data.remove(elem)
        head = rear
    for i in data:
        nn = Node(i)
        nn.link = head
        head = nn
    print("Elements added at the Front end successfully")
    return (head, rear)

def front_deQueue(head, rear):
    if head == None:
        print("Queue is empty")
    else:
        head = head.link
        if head == None:
            rear = None
        print("Element successfully deleted from Front end")
    return (head, rear)

def rear_deQueue(head, rear):
    if rear == None:
        print("Queue is empty")
    else:
        temp = head
        if head != rear:
            while temp.link != rear:
                temp = temp.link
            rear = temp
            rear.link = None
        else :
            rear = None
            head = None
        print("Element successfully deleted from Rear end")
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
    ch = int(input("\nAvailable Operations\n1. Print DEQ\n2. Add Node at FRONT\n3. Delete Node from FRONT\n4. Add Node at REAR\n5. Delete Node from REAR\n6. Search by element\n7. Exit\nEnter your choice : "))
    if ch==1:
        printQueue(head)
    elif ch==2:
        data = input("Enter data in one line, space seperated : ")
        head, rear = front_enQueue(head, rear, data)
    elif ch==3:
        head, rear = front_deQueue(head, rear)
    elif ch==4:
        data = input("Enter data in one line, space seperated : ")
        head, rear = rear_enQueue(head, rear, data)
    elif ch==5 :
        head, rear = rear_deQueue(head, rear)
    elif ch==6 :
        n = input("Enter value to search : ")
        searchQueue(head, n)
    elif ch==7 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
