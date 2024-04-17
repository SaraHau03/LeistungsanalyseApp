import json
from my_functions import estimate_max_hr
from my_classes import Person, Experiment

def main():
    # Eingabe
    experiment_name = input("Art des Experiments: ")
    experiment_number = int(input("Nummer des Experiments: "))
    date = input("Datum des Experiments (DD-MM-YYYY): ")
    supervisor = input("Nachname des Supervisors: ")
    subject_first_name = input("Vorname des Versuchsteilnehmers: ")
    subject_last_name = input("Nachname des Versuchsteilnehmers: ")
    sex = input("Geschlecht des Versuchsteilnehmers (male/female): ")
    age = int(input("Alter des Versuchsteilnehmers: "))
    phone_number = int(input("Telefonnummer des Versuchsteilnehmer: "))

    # Geschätzte maximale Herzfrequenz
    subject = Person(subject_first_name, subject_last_name, sex, age, phone_number)
    max_hr = subject.estimate_max_hr()

    # Experiment-Objekt
    experiment = Experiment(experiment_name, experiment_number, date, supervisor, subject)

    # Ausgabe des Experiment-Dictionary
    print("Experiment- und Versuchsteilnehmerdaten:")
    print(experiment.to_dict())

    # Speichern des Experiment-Objekts in einer JSON-Datei
    filename = "experiment_data.json"
    experiment.save(filename)

    print(f"Die Experiment- und Versuchsteilnehmerdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()