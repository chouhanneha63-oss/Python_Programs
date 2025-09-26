class Company:
    def company_info(self):
        print("Company: Accenture Solutions Pvt Ltd")

class Department(Company):
    def department_info(self):
        print("Department: Data Analytics")

class Employee(Department):
    def employee_info(self):
        print("Employee: Neha Chouhan")
        print("Role: Data Analyst")
        print("Tools: Python, Python Libraries, SQL")

# Create object of the most derived class
emp = Employee()

# Call methods from all levels
emp.company_info()
emp.department_info()
emp.employee_info()
