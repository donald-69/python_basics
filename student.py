from datetime import date, datetime


class Student:
    def __init__(self, name,dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(f"Name: {self.name} , DOB: {self.dob} , Gender: {self.gender}")


    def calculate_age(self):
       age = (datetime.today() - datetime.strptime(self.dob, '%Y-%m-%d'))
       print(age.days//365)
