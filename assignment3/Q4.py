# 4. Multiple Inheritance with Person, Employee, and Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.department = department

manager = Manager("Alice", "M123", "HR")
print(manager.name, manager.emp_id, manager.department)  
