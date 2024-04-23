import json
from datetime import datetime
from my_functions import estimate_max_hr

#Personen:
class Person:
    def __init__(self, first_name, last_name, birth_date, sex):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        self._sex = sex

    def _calculate_age(self):
        today = datetime.now()
        age = today.year - self._birth_date.year - ((today.month, today.day) < (self._birth_date.month, self._birth_date.day))
        return age

    def estimate_max_hr(self):
        age_years = self._calculate_age()
        return estimate_max_hr(age_years, self._sex)

    def to_dict(self):
        max_hr = self.estimate_max_hr()
        return {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "age": self._calculate_age(),
            "sex": self._sex,
            "max_hr": max_hr
        }

    def save(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)

class Subject(Person):
    def __init__(self, first_name, last_name, birth_date, sex):
        super().__init__(first_name, last_name, birth_date, sex)

class Supervisor:
    def __init__(self, id_number):
        self._id_number = id_number

    def to_dict(self):
        return {
            "id_number": self._id_number
        }

    def save(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)

#Experiment:
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
            "supervisor": self.supervisor.to_dict(),
            "subject": self.subject.to_dict() 
        }

    def save(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)