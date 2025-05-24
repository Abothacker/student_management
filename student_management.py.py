#✅ 1. Student Record Management System

students =[]
total_stu = int(input("Enter how many students you want to add: "))
for no, i in enumerate(range(0, total_stu), start=1):
    rollno = int(input(f"Student no : {no} Enter Roll no: "))
    name = input(f"Student no : {no} Enter name: ")
    dict = {"ID": i,"rollno" : rollno,"name" : name}
    students.append(dict)

# show  all info
for i in students:
    print(f'''
    Student info
ID       : {i["ID"]}
Roll no  : {i["rollno"]}
Name     : {i["name"]}''')
    

#Delete by ID
d = input("IF Want delete, type (y): ")
if d.lower == "y":
    idno = int(input("Enter ID to delete : "))
    students.pop(idno)
    print(f"Id {idno} Data Delete succesfully")
else:
    print("NO Delete")


# after all record delete
for i in students:
    print(f'''
    Student info
ID       : {i["ID"]}
Roll no  : {i["rollno"]}
Name     : {i["name"]}''')
    