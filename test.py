import json
from my_classes import Person, Experiment

def main():
    # Testdaten
    experiment_name = "Herzfrequenzmessung"
    experiment_number = 123456
    date = "28-02-2024"
    supervisor = "Hau"
    subject_first_name = "Noah"
    subject_last_name = "Mueller"
    sex = "male"
    age = 20
    phone_number = "621811420"

    # Geschätzte maximale Herzfrequenz
    subject = Person(subject_first_name, subject_last_name, sex, age, phone_number)
    max_hr = subject.estimate_max_hr()

    # Experiment-Objekt
    experiment = Experiment(experiment_name, experiment_number, date, supervisor, subject)

    # Ausgabe des Experiment-Dictionary
    print("Experiment- und Versuchsteilnehmerdaten:")
    print(experiment.to_dict())

    # Speichern des Experiment-Objekts in einer JSON-Datei
    filename = "test_experiment_data.json"
    experiment.save(filename)

    print(f"Die Testdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()
