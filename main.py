from my_classes import Subject, Supervisor, Experiment

def main():
    experiment_name = input("Art des Experiments: ")
    experiment_number = int(input("Nummer des Experiments: "))
    date = input("Datum des Experiments (DD-MM-YYYY): ")

    #Supervisor:
    supervisor_id = input("ID-Nummer des Supervisors: ")
    supervisor = Supervisor(supervisor_id)

    #Subject:
    subject_first_name = input("Vorname des Versuchsteilnehmers: ")
    subject_last_name = input("Nachname des Versuchsteilnehmers: ")
    subject_birth_date = input("Geburtsdatum des Versuchsteilnehmers (DD-MM-YYYY): ")
    subject_sex = input("Geschlecht des Versuchsteilnehmers (male/female): ")
    subject = Subject(subject_first_name, subject_last_name, subject_birth_date, subject_sex)

    #Experiment:
    experiment = Experiment(experiment_name, experiment_number, date, supervisor, subject)

    print("Experiment- und Versuchsteilnehmerdaten:")
    print(experiment.to_dict())

    #Speichern in experiment_data.json:
    filename = "experiment_data.json"
    experiment.save(filename)

    print(f"Die Experiment- und Versuchsteilnehmerdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()