# Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")
import time
file_name = "work.txt"
class Employee:
    def __init__(self, ID, name, contact, department, salary, days_remaining):
        self.ID = ID
        self.name = name
        self.contact = contact
        self.department = department
        self.salary = salary
        self.days_remaining = days_remaining

def add_employee():

    ID = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    contact = input("Enter an e-mail adress or telephone number: ")
    department = input("Enter Employee Department: ")
    salary = input("Enter Employee Salary: ")
    days_remaining = input("Enter Employee Days Remaining: ")
    employee = Employee(ID, name,contact, department, salary, days_remaining)
    with open("work.txt", "a") as file:
        file.write(f"{employee.ID},{employee.name},{employee.contact},{employee.department},{employee.salary},{employee.days_remaining}\n")
        print(f"Personnel with {ID} ID and {name} are registered in the system. Please wait")
        time.sleep(1.5)
        print("Employee added successfully!")
        save()
def give_leave(ID):

    with open("work.txt", "r") as file:
        lines = file.readlines()
        save()
        with open("work.txt", "w") as file:
            employee_found = False
            for line in lines:
                employee = line.strip().split(",")
                if employee[0] == ID:
                    days = int(input("Enter number of days: "))
                    employee_found = True
                    if int(employee[5]) >= days:
                        employee[5] = str(int(employee[5]) - days)
                        file.write(",".join(employee) + "\n")
                        print(f"{days} days leave granted to Employee ID: {ID}. {employee[5]} days remaining.")
                    else:
                        print("The number of days you want to allow is more than the worker's leave entitlement.")
                else:
                    file.write(line)
                    save()
            if not employee_found:
                print("Invalid ID")

def view_employee(ID):

    found = False
    with open("work.txt", "r") as file:
        lines = file.readlines()
        for line in lines[:]:
            employee = line.strip().split(",")
            if employee[0] == ID:
                print(f"All information of the personnel with {ID} are listed, Please wait....")
                time.sleep(2)
                print("ID: ", employee[0])
                print("Name: ", employee[1])
                print("Contact: ", employee[2])
                print("Department: ", employee[3])
                print("Salary: ", employee[4])
                print("Days Remaining: ", employee[5])

                wait =input("Press enter to return to the main menu. If you want to wait longer on this page, "
                            "Please type : YES \n --->")
                if wait == "yes" or wait == "YES" or wait == "Yes":
                    time.sleep(10)
                else:
                    print("You are returned to the Main menu. Please wait...")
                    time.sleep(1.5)
                    return
                found = True
                save()

                break

        if not found:
            print(f"No employee found with this {ID} ID")
            save()


def remove_employee(ID):
    employees = []
    found = False
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            employee = line.strip().split(",")
            if employee[0] != ID:
                employees.append(",".join(employee))
                found = True
        if not found:
            print("Invalid ID")
        with open(file_name, "w") as file:
            for employee in employees:
                file.write(employee + "\n")
            print("Deleting personnel information...Please wait....")
            time.sleep(1.5)
            print(f"Employee with ID: {ID} removed successfully!")
            save()

def update_employee(ID):

    with open("work.txt", "r") as file:
        lines = file.readlines()
        with open("work.txt", "w") as file:
            for line in lines:
                employee = line.strip().split(",")
                if employee[0] == ID:
                    employee[1] = input("Enter new name: ")
                    employee[2] = input("Enter new contact: ")
                    employee[3] = input("Enter new department: ")
                    employee[4] = input("Enter new salary: ")
                    file.write(",".join(employee) + "\n")
                    print(f"Updating information of {ID} personnel. Please wait...")
                    time.sleep(2)
                    print(f"Employee with ID: {ID} and NAME: {employee[1]} are updated successfully!")
                    save()
                else:
                    file.write(line)
                    save()

def update_employee_leave(ID):
    with open("work.txt", "r") as file:
        lines = file.readlines()
        with open("work.txt", "w") as file:
            for line in lines:
                employee = line.strip().split(",")
                if employee[0] == ID:
                    employee[5] = input("Enter remaining days: ")
                    file.write(",".join(employee) + "\n")
                    print("Updating the personal remaining days off.. Please wait")
                    time.sleep(1.5)
                    print(f"Employee with ID: {ID} is updated successfully!")
                    save()
                else:
                    file.write(line)
                    save()
def save():

    with open("work.txt", "r") as file:
        lines = file.readlines()
        with open("work.txt", "w") as file:
            for line in lines:
                file.write(line)

def check_admin_credentials(username, password):
    if username == "admin" and password == "1234":
        print("Logging into account, please wait...")
        time.sleep(1.5)
        print("Login to the system.")
        return True

    elif username == "q" or username == "Q" or password == "Q" or password == "q":
        print("The system has been logged out.")
        quit()
    else:
        print("Wrong username or password...")
        return False

while True:
    print("\nWelcome to company system. We wish you a nice day..\n")
    username = input("Please enter username :")
    password = input("Please enter password : ")
    if check_admin_credentials(username, password):
        while True:

            print("1. Add Employee")
            print("2. Give Leave")
            print("3. View Employee Info")
            print("4. Delete Employee")
            print("5. Update Employee information ")
            print("6. Update Employee leave days")
            print("7. Exit")
            choice = input("Your choice : ")
            if choice == "1":
                add_employee()
            elif choice == "2":
                ID = input("Enter Employee ID: ")

                give_leave(ID)
            elif choice == "3":
                ID = input("Enter Employee ID: ")
                view_employee(ID)
            elif choice == "4":
                ID = input("Enter Employee ID: ")
                remove_employee(ID)
            elif choice == "5":
                ID = input("Enter Employee ID: ")
                update_employee(ID)
            elif choice == "6":
                ID = input("Enter Employee ID: ")
                update_employee_leave(ID)
            elif choice == "7":
                print("EXITING....")
                time.sleep(1.5)
                print("...BYE BYE...")
                save()
                break
            else:
                print("Invalid Input")