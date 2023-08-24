class Employee:
    company = "Google"

    def getSalery(self,signeture):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signeture}")
    

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry=Employee()
harry.salary=100000
harry.getSalery("Thanks!") #Employee.getSalary(harry)
harry.greet() #Employee.greet()
harry.greet()