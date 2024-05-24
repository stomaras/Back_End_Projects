class Employee:
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary
        
    def get_name(self):
        return self._name
    
    def get_position(self):
        return self._position
    
    def get_salary(self):
        return self._salary
    
    def __str__(self):
        return f"{self.get_position()}: {self.get_name()}, Salary ${format(self.get_salary())}"
    

class Department:
    def __init__(self, name):
        self._name = name
        self.children = []
        
    def get_name(self):
        return self._name
    
    def add_child(self, component):
        self.children.append(component)
        
    def remove_child(self, component):
        self.children.remove(component)
        
    # So get employee returns a list of employees that are in the department
    def get_employees(self):
        employees = []
        
        for child in self.children:
            if isinstance(child, Employee):
                employees.append(child)
            elif isinstance(child, Department):
                employees.extend(child.get_employees())
                
        return employees
    
    # get total salary gets the salary of each employee and also add that salary to all the employees
    # in the department to get the total salary of the department
    # returns the total salary of the employee in that department
    
    def get_total_salary(self):
        total_salary = 0
        
        for child in self.children:
            if isinstance(child, Employee):
                total_salary += child.get_salary()
            elif isinstance(child, Department):
                total_salary += child.get_total_salary()
                
        return total_salary
    
    def __str__(self):
        return f"{self.name} ({len(self.children)} employees/department)"
    
    
class Organization:
    
    def chart(self, department, indent=0):
        print(""*indent, f"-{department.get_name()}" \
            f"({len(department.children)})," \
            f"Total Salary:" \
            f"${format(department.get_total_salary(),',')}")
        
        indent += 1
        for child in department.children:
            if isinstance(child, Employee):
                print(''*indent,child)
            elif isinstance(child, Department):
                self.chart(child, indent)
                print()
            
            
# create employees and departments
department1 = Department("Software Engineer")
department1.add_child(Employee('Tom','Software Engineer', 1300))
department1.add_child(Employee('Kostas', 'Software Engineer',1400))

department2 = Department("Sales")
department2.add_child(Employee('Agathi','Sales JR', 880))
department2.add_child(Employee('KwstasKrs','Sales', 900))


executives = Department('Executives')
executives.add_child(Employee('John Smith','CEO', 1000000))
executives.add_child(Employee('Areti','CEO',200000))


print("Organizational Chart / and Salary:")
print("*"*20)

organization = Organization()
organization.chart(department2)