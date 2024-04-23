from my_classes import Subject, Supervisor, Experiment

def main():
    # Erstellung eines Beispiel-Experiment-Objekts
    experiment_name = "Herzfrequenzmessung"
    experiment_number = 123
    date = "05-06-2023"
    supervisor_id = "123456"
    subject_first_name = "Sara"
    subject_last_name = "Hau"
    subject_birth_date = "28-03-2003"
    subject_sex = "female"

    # Erstellung der Objekte
    supervisor = Supervisor(supervisor_id)
    subject = Subject(subject_first_name, subject_last_name, subject_birth_date, subject_sex)
    experiment = Experiment(experiment_name, experiment_number, date, supervisor, subject)

    # Speichern in test_experiment_data.json
    filename = "test_experiment_data.json"
    experiment.save(filename)

    print(f"Die Experimentdaten wurden in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    main()
