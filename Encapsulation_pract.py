class Student:
    def __init__(self, student_id, marks, age):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def validate_marks(self):
        if self.__marks >= 0 & self.__marks<=100:
            return True
        else:
            return False
    
    def validate_age(self):
        if self.__age>=20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.__marks == True & self.__age == True:
            if self.__marks >=65:
                return True
            else:
                return False
        else:
            return False

s1 = Student(1001, 30, 35)
s1.validate_marks()
s1.validate_age()
s1.check_qualification()
