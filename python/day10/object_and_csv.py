import csv

class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def get_details(self):
        return [self.emp_id, self.name, self.age, self.department, self.salary]

# Creating Employee objects
employee = Employee(101, "Alice", 30, "HR", 50000)
# Writing employee data to a CSV file if it doesn't exist, else appending
csv_filename = "employees.csv"

try:
    with open(csv_filename, mode="x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee ID", "Name", "Age", "Department", "Salary"])
except FileExistsError:
    pass

with open(csv_filename, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(employee.get_details())

print(f"Employee data has been appended to {csv_filename}")
