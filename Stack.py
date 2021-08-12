# STACK

class Node :
    def __init__(self, data):
        self.data = data
        self.link = None

def push(head, data): #LL Add at begin
    data = data.split()
    if head==None:
        elem = data[0]
        head = Node(elem)
        data.remove(elem)
    for i in data:
        nn = Node(i)
        nn.link = head
        head = nn
    print("Data added successfully")
    return head

def pop(head):
    if head==None:
        print("Stack is empty")
    else:
        head = head.link
        print("Element popped successfully")
        return head

def printStack(head) :
    print("Print Stack")
    if head == None:
        print("Stack is empty")
    else:
        temp=head
        while temp != None:
            print(temp,' ',temp.data,' ',temp.link)
            temp = temp.link

def searchStack(head, elem):
    if head==None:
        print("Stack is empty")
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
while(True):
    ch = int(input("\nAvailable Operations\n1. Print Stack\n2. Push Node\n3. Pop Node\n4. Search by element\n5. Exit\nEnter your choice : "))
    if ch==1:
        printStack(head)
    elif ch==2:
        data = input("Enter data in one line, space seperated : ")
        head = push(head, data)
    elif ch==3:
        head = pop(head)
    elif ch==4 :
        n = input("Enter value to search : ")
        searchStack(head, n)
    elif ch==5 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again")
