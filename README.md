# Installationsanleitung
- lade den Ordner herunter und öffne den Ordner in Visual Studio Code
- Öffne ein Terminal
- Erstelle eine neue Python-Umgebung
  - `python -m venv .venv`
- Aktiviere die Umgebung 
  - Windows: `.venv\Scripts\Activate`
- Installiere die Pakete
  - Entweder mit `pip install <paketname>`
  - Oder mit `pip install -r requirement.txt`
- Dann wird das Programm mit `python main.py` gestartet

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
    
1. Push & Pull
    -von jmd das geteilte Repository in VS öffnen: File -> New Window -> Clone Repository from GitHub -> link von Github in Suchleiste kopieren
    -Veränderungen von anderen am Repository auf VS sehen: links Source&Control -> ... -> pull
    -geändertes wieder für den anderen comitten: Source&Control -> Änderungen mit Haken anzeigen lassen -> Message eintippen -> und Dateien comitten

2. VENV erstellen: 
    - Virtuelle Umgebung aktivieren, um sicherzustellen, dass die Bedingungen in der Zukunft die selben sind wie aktuell und der Code funktioniert (z.B.: dass sich numpy nicht updated und wir somit unnötige Fehler vermeiden)
    - Virtuelle Umgebung aktivieren mittels /venv
    - in Kommandozeile: <Umgebungsname>\Scripts\activate
    - falls Probleme auftreten: Set-ExecutionPolicy -ExecutionPolicy Unrestricted (hat Sicherheitsgründe)

3. Venv Ordner in Gitignore: 
    -Speichern .gitignore-Datei: Speichern Sie die .gitignore-Datei nachdem Sie den Eintrag für den venv-Ordner hinzugefügt haben.
    -Aktualisieren Sie Ihr Repository: Führen Sie git add .gitignore und git commit -m "Add venv to .gitignore" aus, um Ihre Änderungen an der .gitignore-Datei zu committen (in der Bash Zeile beim Terminal). Danach können Sie Ihr Repository normal pushen
