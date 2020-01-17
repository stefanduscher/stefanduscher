# Programm:     Fenster 3
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

padx : Bereich links und rechts eines Elementes
pady : Bereich über und unter einem Element
"""

# Bibliotheken importieren
from tkinter import * # Komplette Importierung der Bibliothek tkinter


fenster = Tk()

Widgets = [
    Label(master = fenster, text = "Hund", bg = "green",
          font = ("Arial", 12), padx = 10),
    Label(master = fenster, text = "Katze", bg = "blue",
          font = ("Arial", 12), padx = 20, pady = 25),
    Label(master = fenster, text = "Maus", bg = "magenta",
          font = ("Arial", 12), padx = 30, pady = 50)]

for w in Widgets: w.pack()

fenster.mainloop()
    
