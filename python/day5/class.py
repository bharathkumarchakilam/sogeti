class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def set_salary(self,salsry):
        self.salary=salary
        
    def get_salary(self):
        return self.salary
    
emp=employee("bharath",27800)
print("the before update: ",emp.get_salary())
# class employee:
#     def __init__(self,name,salary,allowances,tax_reduction):
#         self.__name=name
#         self.__salary=salary
        
#     def set_salary(self,salsry):
#         self.__salary=salary
        
#     def get_salary(self):
#         return self.__salary
    
#     def set_food_allowances(self):
#         self.__food=food
        
#     def get_food_allowances(self):
#         return self.__food
    
#     def get_transport_allowances(self):
#         self.__transport=transport
     
#     def get_transport_allowances(self):
#         return self.__transport
    
# emp=employee("bharath",27800)
# print("the before update: ",emp.get_salary())