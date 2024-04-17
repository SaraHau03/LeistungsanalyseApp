import json
from my_functions import estimate_max_hr

class Person:
    def __init__(self, first_name, last_name, sex, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.phone_number = phone_number

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
            max_hr_bpm = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age,
            "phone_number": int(self.phone_number)
        }

    def save(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)

class Experiment:
    def __init__(self, experiment_name, experiment_number, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.experiment_number = experiment_number
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def to_dict(self):
        return {
            "experiment_name": self.experiment_name,
            "experiment_number": self.experiment_number,
            "date": self.date,
            "supervisor": self.supervisor,
            "subject": self.subject.to_dict() 
        }

    def save(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)
