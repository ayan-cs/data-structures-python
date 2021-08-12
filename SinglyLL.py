# LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

def printLL(head) :
    print("Print LL")
    if head == None:
        print("LL is empty")
    else:
        temp=head
        while temp != None:
            print(temp,' ',temp.data,' ',temp.link)
            temp = temp.link

def insertNode(head, data):
    data = data.split()
    if head==None:
        elem = data[0]
        head = Node(elem)
        data.remove(elem)
    temp=head
    while temp.link != None:
        temp = temp.link
    for i in data:
        nn = Node(i)
        temp.link = nn
        temp = temp.link
    print("Data added successfully")
    return head

def deleteNode(head, data):
    flag=0
    if head.data == data:
        head = head.link
        flag=1
    else :
        prev = head
        temp = head.link
        while temp != None:
            if temp.data == data:
                prev.link = temp.link
                flag=1
                break
            else :
                prev = temp
                temp = temp.link
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
            head = head.link
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

