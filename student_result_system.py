student_list = []

def add_student(id, n, m):
    student = {
        "id" : id,
        "name" : n,
        "marks" : m
    }
    student_list.append(student)
    


def searchById(id):
    for student in student_list:
        s_id = student["id"]
        if(s_id == id):
            return student
        


        
choice = 1
while(choice):
    print("enter any option: \n")
    option  = input("1.Add student\n2. Search Student")
    if option == '1':
        id = int(input("enter Id: "))
        n = input("enter name: ")
        m = int(input("enter marks: "))
        add_student(id, n, m)
    
    elif option == '2':
        id = int(input("enter student id"))
        result = searchById(id)
        if result :
            print(result)
        else:
            print("no such id exist!!")
        
    else:
        print("invalid option")
        
    
    choice = int(input("\ncontinue?  --- choose 0 or 1: "))


