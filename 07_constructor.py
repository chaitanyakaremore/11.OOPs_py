class Employee:
    compny="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"salary of this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry=Employee("Harry",100, "YouTube")
#harry= employee()-->This throws error(missing 3 is required positional argument:)
harry.getDetails()