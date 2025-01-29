class worker:
    def __init__(self, name):  
        self.name = name
        
class employee(worker):
    def set_name(self, name):
        self.__name = name
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
    def get_salary(self):
        if hasattr(self, "_employee__name") and self.__name != "": 
            return self.__salary
    def get_allowances(self, allowances):
        self.__salary = self.__salary + sum(allowances)  
        return self.__salary
    def get_deductions(self, deductions):
        for i in deductions:
            subst = (i * self.__salary) / 100
            self.__salary = self.__salary - subst  
        return self.__salary

def main():
    employee1 = employee(input("Enter the name of the employee: "))
    employee1.set_salary(int(input("Enter the salary: ")))
    print("The total salary with food and travel expenses: ", employee1.get_allowances([2000, 3000]))
    print("The salary after all deductions is: ", employee1.get_deductions([20]))

main()
