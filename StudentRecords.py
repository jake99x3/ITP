"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""

import csv

student_details = ['ID', 'name', 'age', 'email', 'phone', 'address']
database = 'students.csv'

def menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_details
    global database

    student_data = []
    for field in student_details:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_details
    global database

    print("--- Student Records ---")

    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_details:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global database

    print("--- Search Student ---")
    ID = input("Enter ID no. to search: ")
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----- Student Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("Address: ", row[5])
                    break
        else:
            print("ID No. not found in our database")
    input("Press any key to continue")


def update_student():
    global student_details
    global database

    print("--- Update Student ---")
    roll = input("Enter ID no. to update: ")
    index_student = None
    updated_data = []
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    student_data = []
                    for field in student_details:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

def delete_student():
    global student_details
    global database

    print("--- Delete Student ---")
    roll = input("Enter ID no. to delete: ")
    student_found = False
    updated_data = []
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
    if student_found is True:
        with open(database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID no. ", roll, "deleted successfully")
    else:
        print("ID No. not found in our database")

    input("Press any key to continue")


while True:
    menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("END OF FINAL")
