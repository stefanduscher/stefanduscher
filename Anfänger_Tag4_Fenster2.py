# Programm:     Fenster 2
#
# Datum:        11.10.2019
#
# Autor:        Stefan Duscher
#
# Bemerkungen:  Beispiel VHS-Kurs zum Einsatz eines GUI (graphic user interface)
#
# ---------------------------------------------------------------------------------
"""
Widgets sind alle Bausteine, mit denen man dann eine grafische Oberfläche
zusammensetzt.

Label ist zum Beispiel ein Widget. In einem Label kann ein Text oder ein
Bild positioniert werden.
"""




# Importieren der Bibliothek tkinter
# Diese Bibliothek stellt alle Funktionen zur Verfügung, um mittels
# Fenstern mit dem Bediener zu kommunizieren (Ein- und Ausgabe)
from tkinter import * # Komplette Importierung der Bibliothek tkinter



# Hier wird die Prozedur (ist eine Funktion ohne Return) definiert,
# die dem Label-Widget den Beschriftungstext "Hallo Welt" zuweist
def gruessen():
    label.config(text = "Hallo Welt !")

fenster = Tk() # Instanzieren des Fensters als Objekt der Klasse Tk
label = Label(fenster, text = "Gruss") # Ein Label wird erzeugt
label.pack()    # Das Label wird mit dem Fenster "vereint"
knopf = Button(master = fenster, text = "Hallo sagen", command = gruessen) # Ein Druckknopf wird erzeugt
knopf.pack()    # Der Druckknopf wird mit dem Fenster "vereint"

# --- Hauptprogramm ---
fenster.mainloop() # Aktivierung des Fensters; ab jetzt ist es aktiv
