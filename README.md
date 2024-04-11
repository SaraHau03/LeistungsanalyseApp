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
    -geändertes wieder für den anderen comitten: Source&Control -> Änderungen sollten angezeigt werden -> Message eintippen -> und Dateien comitten

2. VENV erstellen:
    - Virtuelle Umgebung aktivieren, um sicherzustellen, dass die Bedingungen in der Zukunft die selben sind wie aktuell und der Code funktioniert (z.B.: dass sich numpy nicht updated und wir somit unnötige Fehler vermeiden)
    - Virtuelle Umgebung aktivieren mittels /venv
    - in Kommandozeile: <Umgebungsname>\Scripts\activate
    - falls Probleme auftreten: Set-ExecutionPolicy -ExecutionPolicy Unrestricted (hat Sicherheitsgründe)

3. Venv Ordner in Gitignore: 
    -Speichern Sie Ihre .gitignore-Datei: Speichern Sie die .gitignore-Datei nachdem Sie den Eintrag für den venv-Ordner hinzugefügt haben.
    -Aktualisieren Sie Ihr Repository: Führen Sie git add .gitignore und git commit -m "Add venv to .gitignore" aus, um Ihre Änderungen an der .gitignore-Datei zu committen. Danach können Sie Ihr Repository normal pushen
