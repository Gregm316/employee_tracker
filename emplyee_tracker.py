class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

class EmployeeTracker:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, position):
        employee = Employee(emp_id, name, position)
        self.employees.append(employee)
        print("Employee added successfully!")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("Employee List:")
            for employee in self.employees:
                print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}")

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print(f"Employee found - ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}")
                return employee
        print("Employee not found.")
        return None

    def edit_employee(self, emp_id, new_name=None, new_position=None):
        employee = self.search_employee(emp_id)
        if employee:
            if new_name:
                employee.name = new_name
            if new_position:
                employee.position = new_position
            print("Employee details updated successfully!")
        else:
            print("Unable to update. Employee not found.")

def main():
    tracker = EmployeeTracker()
    while True:
        print("\nEmployee Tracker")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search Employee")
        print("4. Edit Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            tracker.add_employee(emp_id, name, position)

        elif choice == "2":
            tracker.list_employees()

        elif choice == "3":
            emp_id = input("Enter employee ID to search: ")
            tracker.search_employee(emp_id)

        elif choice == "4":
            emp_id = input("Enter employee ID to edit: ")
            new_name = input("Enter new name (leave blank to keep current name): ")
            new_position = input("Enter new position (leave blank to keep current position): ")
            tracker.edit_employee(emp_id, new_name if new_name else None, new_position if new_position else None)

        elif choice == "5":
            print("Exiting the Employee Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
