class Employee:
    company="Google"

harry = Employee()
rajani=Employee()
print(harry.company)
print(rajani.company)
Employee.company="youtube"
print(harry.company)
print(rajani.company)

