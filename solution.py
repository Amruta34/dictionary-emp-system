# Solution
employees = {}
def add_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists.")
        return
    name = input("Enter Name: ")
    if not name.replace(" ", "").isalpha():
        print("Invalid name format.")
        return
    age = input("Enter Age: ")
    if not age.isdigit() or int(age) <= 0:
        print("Invalid age format. Age must be a positive integer.")
        return
    department = input("Enter Department: ")
    employees[emp_id] = {"name": name, "age": int(age), "department": department}
    print("Employee added successfully.")
def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee ID not found.")
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee ID not found.")
        return
    print("Current Details:", employees[emp_id])
    name = input("Enter New Name (Leave blank to skip): ")
    if name and not name.replace(" ", "").isalpha():
        print("Invalid name format.")
        return
    age = input("Enter New Age (Leave blank to skip): ")
    if age and (not age.isdigit() or int(age) <= 0):
        print("Invalid age format. Age must be a positive integer.")
        return
    department = input("Enter New Department (Leave blank to skip): ")
    if name:
        employees[emp_id]["name"] = name
    if age:
        employees[emp_id]["age"] = int(age)
    if department:
        employees[emp_id]["department"] = department
    print("Employee updated successfully.")
def search_employee():
    search_type = input("Search by [1] ID or [2] Name: ")
    if search_type == '1':
        emp_id = input("Enter Employee ID: ")
        print(employees.get(emp_id, "Employee not found."))
    elif search_type == '2':
        name = input("Enter Employee Name: ").lower()
        found = False
        for emp_id, details in employees.items():
            if details['name'].lower() == name:
                print(f"{emp_id}: {details}")
                found = True
        if not found:
            print("Employee not found.")
def sort_employees():
    sort_type = input("Sort by [1] Name, [2] Age, [3] Department: ")
    sorted_employees = list(employees.items())

    if sort_type == '1':
        sorted_employees.sort(key=lambda x: x[1]['name'])
    elif sort_type == '2':
        sorted_employees.sort(key=lambda x: x[1]['age'])
    elif sort_type == '3':
        sorted_employees.sort(key=lambda x: x[1]['department'])
    else:
        print("Invalid choice.")
        return
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details}")
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee Details")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            search_employee()
        elif choice == '5':
            sort_employees()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu()
