class Employee:
    count = 0
    sal = 0

    def __init__(self, name, family, sal, dept):
        self.name = name
        self.family = family
        Employee.sal += sal
        self.dept = dept
        Employee.count += 1

    def display(self):
        print("total employees = ", Employee.count)

    def avg_sal(self):
        avg_sal = Employee.sal / Employee.count
        print("average salary of employee :", avg_sal)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, sal, dept):
        print('this is the subclass: Full time employee')
        Employee.__init__(self, name, family, sal, dept)


e1 = Employee('chaitanya', 'A', 10000, 'CS')
e2 = Employee('sailesh', 'B', 30000, 'IT')
e3 = Employee('tondepu', 'C', 80000, 'CSE')
e4 = FullTimeEmployee('chaitu', 'D', 120000, 'CIVIL')

e4.display()
e4.avg_sal()
