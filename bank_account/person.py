import string
from exceptions import PersonTypeError, PersonValueError

gender_list = ["Male", "Female", "male", "female"]  # Սա փորձեցի որպես կլասի փոփոխական գրել չճանաչեց


class Person:
    def __init__(self, name: str, surname, age, gender, email):
        try:
            if type(name) != str:
                raise PersonTypeError("name", name)
            elif type(surname) != str:
                raise PersonTypeError("surname", surname)
            elif type(age) != int:
                raise PersonTypeError("age", age)
            elif type(email) != str:
                raise PersonTypeError("email", email)

            for i in name:
                if i not in string.ascii_letters:
                    raise PersonValueError("name", name)
            for i in surname:
                if i not in string.ascii_letters:
                    raise PersonValueError("surname", surname)
            if age < 0 or age > 110:
                raise PersonValueError("age", age)
            elif gender not in gender_list:
                raise PersonTypeError("gender", gender)
        except PersonTypeError as err:
            print(err)
        except PersonValueError as err:
            print(err)
        else:
            self.name = name
            self.surname = surname
            self.age = age
            self.gender = gender
            self.email = email

    def __repr__(self):
        try:
            return "{} {} - {} , Gender '{}', Email-{}".format(self.name, self.surname, self.age, self.gender, self.email)
        except AttributeError:
            return "Object is empty."

    def add_age(self, n=1):
        self.age += n

