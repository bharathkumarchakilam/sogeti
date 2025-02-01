from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    def __init__(self, name: str, salary: float, role: str):
        self.name = name
        self.salary = salary
        self.role = role

    @abstractmethod
    def work(self) -> str:
        pass
    
    def get_salary(self) -> float:
        return self.salary

# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Manager")

    def work(self) -> str:
        return f"{self.name} is managing the team."

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Developer")

    def work(self) -> str:
        return f"{self.name} is writing code."

class Intern(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Intern")

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

class Security(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Security")

    def work(self) -> str:
        return f"{self.name} is securing the assets."

# Step 3: Define Department class that manages Employees
class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired as a {employee.role}.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired from {employee.role} position.")
    
    def promote(self, employee: Employee) -> None:
        if employee.role == "Intern":
            employee.role = "Developer"
            employee.salary += 20000
        elif employee.role == "Developer":
            employee.role = "Manager"
            employee.salary += 30000
        else:
            print(f"{employee.name} cannot be promoted further.")
            return
        print(f"{employee.name} has been promoted to {employee.role} with a salary of {employee.salary}.")
    
    def demote(self, employee: Employee) -> None:
        if employee.role == "Manager":
            employee.role = "Developer"
            employee.salary -= 30000
        elif employee.role == "Developer":
            employee.role = "Intern"
            employee.salary -= 20000
        else:
            print(f"{employee.name} cannot be demoted further.")
            return
        print(f"{employee.name} has been demoted to {employee.role} with a salary of {employee.salary}.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:\n")
        for employee in self.employees:
            print(f"Employee name: {employee.name}\n, Salary: {employee.get_salary()}\n, Role: {employee.role}\n, Task: {employee.work()}\n")

# Step 4: Create department and add employees
# Create employees
manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 30000)
securitystaff = Security("Ram", 5000)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)

# Show employee details
it_department.show_employee_details()

# Promote an employee
it_department.promote(intern)
it_department.promote(developer)

# Demote an employee
it_department.demote(manager)

# Show details after promotion and demotion
it_department.show_employee_details()

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")

