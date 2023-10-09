'''Task3. Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.
In addition to creating a class, display information about the base classes from which
the employee class is inherited (__base__), the class namespace (__dict__), the
class name (__name__), the module name in which the class is defined
(__module__), the documentation bar ( __doc__)'''
class Employee:
    # Class variable to keep track of the total number of employees
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

# Create instances of the Employee class
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# Display information about each employee
employee1.display_employee_info()
employee2.display_employee_info()

# Display the total number of employees
Employee.display_total_employees()

# Display information about the class itself
print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation string: {Employee.__doc__}")