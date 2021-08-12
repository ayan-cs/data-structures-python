# STUDENTS RECORD

class Student :
    def __init__(self, roll, name, program, stream, startyear, gradyear):
        self.roll = str(roll)
        self.name = str(name)
        self.program = str(program)
        self.stream = str(stream)
        self.startyear = int(startyear)
        self.gradyear = int(gradyear)

    def updateRoll(self, newRoll):
        self.roll = newRoll

    def updateName(self, newName):
        self.name = newName

    def updateProgram(self, newProgram):
        self.program = newProgram

    def updateStream(self, newStream):
        self.stream = newStream

    def updateStartYear(self, newStartYear):
        self.startyear = newStartYear

    def updateGradYear(self, newGradYear):
        self.gradyear = newGradYear

    def showData(self):
        print(f"Roll No. : {self.roll}\tName : {self.name}\tProgram : {self.program}\tStream : {self.stream}\tSession : {self.startyear}-{self.gradyear}")

def viewByRoll(roll):
    flag=0
    for i in all_students :
        if i.roll == roll :
            print(i.showData())
            flag=1
            break
    if flag==0:
        print("Student not found")

def addStudent(n):
    stu_list=[]
    for i in range(n) :
        print(f"\nEnter details of Student {i+1}")
        roll = input("Roll number to be assigned : ")
        name = input("Name : ")
        prog = input("Selected Program: ")
        stream = input("Stream : ")
        start = int(input("Start year : "))
        end = int(input("Expected end year : "))
        temp = Student(roll, name, prog, stream, start, end)
        stu_list.append(temp)
    return stu_list

def updateRecord(i):
    print(f"The student's existing details are")
    print(i.showData())
    ch = int(input("Enter which field you want to update\n1. Roll Number\n2. Name\n3. Program\n4. Stream\n5. Start Year\n6. End Year\nEnter your choice : "))
    if ch==1:
        temp = input("Enter new Roll number : ")
        for x in all_students:
            if x.roll == temp:
                print("Roll Number already assigned/exists")
                break
            else :
                i.updateRoll(temp)
                print("Roll number successfully updated")
                break
    elif ch==2:
        temp = input("Enter correct Name : ")
        i.updateName(temp)
        print("Name successfully updated")
    elif ch==3 :
        temp = input("Enter new Program : ")
        i.updateProgram(temp)
        print("Program successfully updated")
    elif ch==4 :
        temp = input("Enter new Stream : ")
        i.updateStream(temp)
        print("Stream successfully updated")
    elif ch==5 :
        temp = input("Enter correct Start year : ")
        i.updateStartYear(temp)
        print("Start Year successfully updated")
    elif ch==6 :
        temp = input("Enter correct End Year : ")
        i.updateEndYear(temp)
        print("End Year successfully updated")
    else :
        print("Invalid choice")
    return i



all_students=[]
while(1):
    ch = int(input("\nAvailable Operations :\n1. Print ALL Records\n2. View by Roll Number\n3. Add a Record\n4. Update a Record\n5. Delete a Record\n6. Exit\nEnter your choice : "))
    if ch==1:
        if len(all_students)==0 :
            print("No records found")
        else:
            for i in all_students:
                i.showData()
    elif ch==2 :
        roll = input("Enter a valid Roll Number : ")
        viewByRoll(roll)
    elif ch==3 :
        n = int(input("Enter how many students : "))
        all_students+=addStudent(n)
    elif ch==4 :
        flag=0
        roll = input("Enter a valid roll number : ")
        for i, stu in enumerate(all_students) :
            if stu.roll == roll :
                all_students[i] = updateRecord(stu)
                flag=1
                break
        if flag==0:
            print("Student not found")
    elif ch==5 :
        flag=0
        roll = input("Enter a valid roll number : ")
        for i in all_students :
            if i.roll == roll :
                all_students.remove(i)
                flag=1
                break
        if flag==0:
            print("Student not found")
    elif ch==6 :
        import sys
        sys.exit()
    else:
        print("Invalid Choice. Please try again.")
