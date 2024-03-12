from model.Person import Person
from model.Animal import Animal
from model.Rectangle import Rectangle
from model.Employee import Employee
import numpy as np
import pandas as pd

if __name__ == '__main__':

    #1

    student_1 = Person("gal", "milon", 30, 1.92, 80, [])
    student_2 = Person("avi", "cohen", 31, 1.85, 70, [])
    student_3 = Person("sarah", "imenu", 200, 5.92, 3, [])

    print("Class type of student_1:", type(student_1))
    print("Class type of student_2:", type(student_2))
    print("Class type of student_3:", type(student_3))

    print(student_1.name)
    student_1.name = "Gal"
    print(student_1.name)

    print(student_2.last_name)
    student_2.last_name = "C"
    print(student_2.last_name)

    #2
    milo = Animal("milo", "canine", "Black", 10, 25)

    student_1.add_pet(milo)
    student_1.print_attributes()
    student_1.remove_pet("milo")
    student_1.print_attributes()

    #3
    rectangle = Rectangle(2,3)
    print(rectangle.get_area())

    #4
    employee1 = Employee("John Doe", 2015, 60000, "123 Main St, Anytown")
    employee2 = Employee("Jane Smith", 2018, 70000, "456 Elm St, Othertown")
    employee3 = Employee("Bob Johnson", 2017, 65000, "789 Oak St, Anothertown")

    employees_df = [employee1.__dict__, employee2.__dict__, employee3.__dict__]

    df = pd.DataFrame(employees_df)

    print(df.to_string(index=False))