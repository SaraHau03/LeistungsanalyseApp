import json
from my_functions import estimate_max_hr, build_person, build_experiment

def main():
    # Eingabe
    experiment_name = input("Art des Experiments: ")
    experiment_number = int(input("Nummer des Experiments: "))
    date = input("Datum des Experiments (DD-MM-YYYY): ")
    supervisor= input("Nachname des Supervisors: ")
    subject_first_name = input("Vorname des Versuchsteilnehmers: ")
    subject_last_name = input("Nachname des Versuchsteilnehmers: ")
    sex = input("Geschlecht des Versuchsteilnehmers (male/female): ")
    age = int(input("Alter des Versuchsteilnehmers: "))
    phone_number = int(input("Telefonnummer des Versuchsteilnehmer: "))

    # Geschätzte maximale Herzfrequenz
    max_hr = int(estimate_max_hr(age, sex))

    # Dictionary für den Versuchsteilnehmer
    subject = build_person(subject_first_name, subject_last_name, sex, age, phone_number)

    # Experiment-Dictionary
    experiment_dict = build_experiment(experiment_name, experiment_number, date, supervisor, subject)

    # Ausgabe des Experiment-Dictionary
    print("Experiment- und Versuchsteilnehmerdaten:")
    print(experiment_dict)

    # Speichern des Experiment-Dictionary in einer JSON-Datei
    filename = "experiment_data.json"
    with open(filename, "w") as outfile:
        json.dump(experiment_dict, outfile)

    print(f"Die Experiment- und Versuchsteilnehmerdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()