# Vorgehen LeistungsanalyseApp:
 In VS-Code Dateien erstellen:
    - .gitignore -> zum Verstecken von Venv
    - README.md -> zum Arbeit nachvollziehen
    - main.py -> Aus dem Unterprogramm werden Funktion zur Berechnung verschiedener Messwerte genutzt und in dem Hauptprogramm genutzt, um die Analyse durchzuführen und kompakt in einem Dictionary zu speichern
    - experiment_data.json -> ist ein angelegtes Dictionary welches Daten über Probanden beinhaltet und die ausgegebenen Daten der Analyse dort speichert
    - my_functions.py -> beinhaltet alle 3 Berechnungsfunktionen um die eingegebenen Daten zu verarbeiten

#  Benutzung der App:
    - Benutzer muss verschieden Daten eingeben (siehe fkt .main)
    - Experiment und Daten der Person werden gespeichert

# Nice to know:
    -von jmd das geteilte Repository in VS öffnen: File -> New Window -> Clone Repository from GitHub -> link von Github in Suchleiste kopieren
    -Veränderungen von anderen am Repository auf VS sehen: links Source&Control -> ... -> pull
    -Virtuelle Umgebung aktivieren, um sicherzustellen, dass die Bedingungen in der Zukunft die selben sind wie aktuell und der Code funktioniert (z.B.: dass sich numpy nicht updated und wir somit unnötige Fehler vermeiden)
    - Virtuelle Umgebung aktivieren mittels /venv
    - in Kommandozeile: <Umgebungsname>\Scripts\activate
    - falls Probleme auftreten: Set-ExecutionPolicy -ExecutionPolicy Unrestricted (hat Sicherheitsgründe)

    -> VENV erstellen:

