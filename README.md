# 📋 quicknote

## 📋 Overview
This program is a simple but flexible note-taking app with a user-friendly interface. 

It allows:

* Saving notes with title, content and tags in a JSON file.
* Editing tags via a special dialog window.
* Switching between Dark Mode and Light Mode.
* Creating a JSON file when you start it for the first time by entering the file name and creator.
* Automatically use the first available tag if the user does not select a tag when creating a note.

## ⚙️ Voraussetzungen
* Python 3.x needs to be installed.
* The standard Tkinter library is required (usually included with Python).
* Python modules: datetime, json, os

## 📦 Installation
Klone das Repository oder kopiere die Quelldatei:

bash
Code kopieren
git clone <REPOSITORY-URL>
cd <ORDNER>
Starte das Programm:

bash
Code kopieren
python notizen_app.py
Beim ersten Start wird eine JSON-Datei erstellt.

🧩 Funktionen
1. Erstellen der JSON-Datei beim ersten Start
Wenn noch keine JSON-Datei vorhanden ist, erscheint ein Popup.
Der Benutzer gibt einen Dateinamen und den Ersteller ein.
Die Datei wird erstellt und enthält:
Name des Erstellers
Letztes Bearbeitungsdatum
Standard-Tags: Wichtig, Privat, Arbeit, Sonstiges
Beispielinhalt der JSON-Datei:
json
Code kopieren
{
  "ersteller": "Max Mustermann",
  "letztes_bearbeitungsdatum": "2024-06-17 12:00:00",
  "tags": ["Wichtig", "Privat", "Arbeit", "Sonstiges"],
  "notizen": []
}
2. Notizen erstellen
Gib einen Titel und Inhalt der Notiz ein.
Wähle ein Tag aus dem Dropdown-Menü.
Wenn kein Tag ausgewählt wird, wird automatisch das erste Tag aus der Tag-Liste verwendet.
Klicke auf den Submit-Button, um die Notiz zu speichern.
Die Notiz wird in der JSON-Datei gespeichert und enthält:
Titel
Inhalt
Tag
Datum der Erstellung
3. Tag-Verwaltung
Neben dem Dropdown-Menü für Tags befindet sich ein Zahnrad-Button ⚙. Ein Klick öffnet den Tag-Manager:

Tags anzeigen: Die aktuellen Tags werden in einer Liste dargestellt.
Tags löschen: Jedes Tag hat einen Mülleimer-Button 🗑 zum Löschen.
Tags hinzufügen: Gib einen neuen Tag in das Textfeld ein und klicke auf den Plus-Button ➕.
Änderungen werden in der JSON-Datei gespeichert, und das Dropdown-Menü wird aktualisiert.
4. Dark Mode und Light Mode umschalten
Ein Button mit 🌙 (Mond-Symbol) zeigt den aktuellen Dark Mode an.
Ein Klick wechselt zu Light Mode (Sonnen-Symbol ☀) und aktualisiert die Farben der Oberfläche.
Das Theme bleibt für die aktuelle Sitzung aktiv.
🌟 Bedienung
Starte das Programm.
Erstelle beim ersten Start eine JSON-Datei.
Füge Notizen hinzu und verwalte Tags.
Wechsle bei Bedarf zwischen Dark Mode und Light Mode.
📄 Lizenz
Dieses Projekt steht unter der MIT-Lizenz.

🛠 Screenshots
Hier kannst du bei Bedarf Screenshots der Anwendung hinzufügen.

📧 Kontakt
Bei Fragen oder Feedback kannst du dich gerne an den Entwickler wenden.

Anpassungen in der Funktionalität:
Wenn beim Erstellen einer Notiz kein Tag ausgewählt wird, übernimmt das Programm automatisch das erste Tag aus der Tag-Liste als Standardwert.