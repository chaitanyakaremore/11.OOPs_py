class Employee:
    company="Google"
    def getSalery(self):
        print(f"Salary for this employee working in {self.company} is {self.salery}")

harry = Employee()
harry.salery=100000
harry.getsalary()  #Employee.getSalery(harry)