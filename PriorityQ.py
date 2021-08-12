# PRIORITY QUEUE

class Node :
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.link = None

def printQueue(head) :
    print("Print Queue")
    if head == None:
        print("Queue is empty")
    else:
        while head != None:
            print(head,' ',head.data,' ',head.priority,' ',head.link)
            head = head.link

def searchQueue(head):
    if head==None:
        print("Queue is empty")
    else:
        elem = input("Enter value to search : ")
        loc=[]
        pr=[]
        i=1
        while head != None:
            if head.data == elem:
                loc.append(i)
                pr.append(head.priority)
            i+=1
            head = head.link
        if len(loc)==0:
            print("Element not found")
        else:
            print(f"Element found at positions : {loc} with Priorities {pr} respectively")

def findMaxPriority(head) :
    priority=[]
    while head != None:
        priority.append(head.priority)
        head = head.link
    return max(priority)

def isPriorityExist(head, pr):
    while head!= None:
        if head.priority == pr:
            return True
        head = head.link
    return False

def deQueue(head):
    if head == None:
        print("Queue is empty")
        return head
    if head.link == None :
        print(f"Element {head.data} with Priority {head.priority} deleted successdully")
        return None
    maxpr = findMaxPriority(head)
    prev = None
    temp = head
    if head.priority == maxpr :
        print(f"Element {head.data} with Priority {head.priority} deleted successdully")
        head = head.link
        return head
    while temp.priority != maxpr:
        prev = temp
        temp = temp.link
    prev.link = temp.link
    print(f"Element {temp.data} with Priority {temp.priority} deleted successdully")
    return head

def enQueue(head, data, priority):
    if head == None:
        head = Node(data, priority)
        return head
    if isPriorityExist(head, priority)==True:
        print("Priority value exists. Try some different value.")
        return head
    nn = Node(data, priority)
    temp = head
    while temp.link != None :
        temp = temp.link
    temp.link = nn
    print("Element added successfully")
    return head

ch = -1
head = None
while(True):
    ch = int(input("\nAvailable Operations\n1. Print LL\n2. Add Node\n3. Delete Node\n4. Search by element\n5. Exit\nEnter your choice : "))
    if ch==1:
        printQueue(head)
    elif ch==2:
        data = input("Enter data : ")
        priority = int(input("Enter priority : "))
        head = enQueue(head, data, priority)
    elif ch==3:
        head = deQueue(head)
    elif ch==4 :
        searchQueue(head)
    elif ch==5 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
