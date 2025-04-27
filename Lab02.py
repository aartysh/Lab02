class Employee:
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Office(Employee):

    def __init__(self,firstName, lastName, position):
        super().__init__(firstName, lastName)
        self.position = position
        self.empList = []


    def addEmployee(self, emp):
        self.empList.append(emp)

    def removeEmployee(self,emp):
        try:
            self.empList.remove(emp)
        except:
            print("Wrong employee name")

    def show(self):
        sortedEmployees = sorted(self.empList, key = lambda em: em.lastName)
        for em in sortedEmployees:
            print(em)

    def changeEmp(self,index, newFirstName, newLastName, NewPosition):
        emp = self.empList[index]
        try:
            emp.firstName = newFirstName
            emp.lastName = newLastName
            emp.position = NewPosition
        except:
            print("not enought argument")

#Example

office = Office("1", "2", "3")


emp1 = Office("John", "Smith", "Engineer")
emp2 = Office("Anna", "Taylor", "Designer")
emp3 = Office("Mark", "Brown", "Technician")


office.addEmployee(emp1)
office.addEmployee(emp2)
office.addEmployee(emp3)


print("Employees list:")
office.show()


office.changeEmp(1, "Anna", "Green", "Senior Designer")


office.removeEmployee(emp3)


office.show()






    

