# Parent Class
class Employee:

    # Constructor
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    # Employee Details
    def show_details(self):

        print("\n----- Employee Details -----")
        print("Name:", self.name)
        print("Salary:", self.salary)

    # Salary Calculation
    def calculate_salary(self):

        return self.salary


# Child Class 1
class Manager(Employee):

    # Constructor
    def __init__(self, name, salary, bonus):

        # Parent constructor call
        super().__init__(name, salary)

        self.bonus = bonus

    # Method Overriding
    def calculate_salary(self):

        total = self.salary + self.bonus

        return total


# Child Class 2
class Developer(Employee):

    # Constructor
    def __init__(self, name, salary, overtime):

        super().__init__(name, salary)

        self.overtime = overtime

    # Method Overriding
    def calculate_salary(self):

        total = self.salary + self.overtime

        return total


# Object Creation
emp1 = Manager("Shashi", 50000, 10000)

emp2 = Developer("Rahul", 40000, 5000)

# Show Details
emp1.show_details()

print("Total Salary:", emp1.calculate_salary())

emp2.show_details()

print("Total Salary:", emp2.calculate_salary())