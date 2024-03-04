import json

# Employee class to represent an employee
class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department
    
    # Method to display employee details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")
    
    # String representation method to return employee's name and ID
    def __str__(self):
        return f"{self.name} - {self.emp_id}"

# Department class to represent a department
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    # Method to add an employee to the department
    def add_employee(self, employee):
        self.employees.append(employee)
    
    # Method to remove an employee from the department
    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False
    
    # Method to list all employees in the department
    def list_employees(self):
        for employee in self.employees:
            print(employee)
    
# Company class to represent the company
class Company:
    def __init__(self):
        self.departments = {}
    
    # Method to add a department to the company
    def add_department(self, department):
        self.departments[department.name] = department
    
    # Method to remove a department from the company
    def remove_department(self, name):
        if name in self.departments:
            del self.departments[name]
            return True
        return False
    
    # Method to display all departments and their employees
    def display_departments(self):
        for name, department in self.departments.items():
            print(f"Department: {name}")
            department.list_employees()
            print()
    
    # Method to save company data to a file
    def save_company_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.departments, file, default=lambda o: o.__dict__, indent=4)
    
    # Method to load company data from a file
    def load_company_data(self, filename):
        with open(filename, 'r') as file:
            self.departments = json.load(file)
            for name, dept_data in self.departments.items():
                department = Department(name)
                for emp_data in dept_data['employees']:
                    employee = Employee(**emp_data)
                    department.add_employee(employee)
                self.departments[name] = department

# Function to print the menu for user interaction
def print_menu():
    print("Employee Management System Menu")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Exit")

# Main function to run the program
def main():
    # Create a Company object
    company = Company()
    try:
        # Load company data from file if exists
        company.load_company_data("company_data.json")
        print("Company data loaded successfully.")
    except FileNotFoundError:
        print("No existing company data found.")
    
    while True:
        # Display menu options
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Employee
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter employee department: ")
            employee = Employee(name, emp_id, title, department)
            if department in company.departments:
                company.departments[department].add_employee(employee)
                print("Employee added successfully.")
            else:
                print("Department does not exist.")
        
        elif choice == "2":
            # Remove Employee
            department = input("Enter department name: ")
            emp_id = input("Enter employee ID to remove: ")
            if department in company.departments:
                if company.departments[department].remove_employee(emp_id):
                    print("Employee removed successfully.")
                else:
                    print("Employee not found.")
            else:
                print("Department does not exist.")
        
        elif choice == "3":
            # Display Department
            department = input("Enter department name: ")
            if department in company.departments:
                print(f"Employees in {department} department:")
                company.departments[department].list_employees()
            else:
                print("Department does not exist.")
        
        elif choice == "4":
            # Add Department
            department = input("Enter department name to add: ")
            new_department = Department(department)
            company.add_department(new_department)
            print("Department added successfully.")
        
        elif choice == "5":
            # Remove Department
            department = input("Enter department name to remove: ")
            if company.remove_department(department):
                print("Department removed successfully.")
            else:
                print("Department does not exist.")
        
        elif choice == "6":
            # Exit program and save company data
            company.save_company_data("company_data.json")
            print("Company data saved successfully.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
