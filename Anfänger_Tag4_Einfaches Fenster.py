# Programm:     Einführung Fenster
#
# Datum:        09.10.2019
#
# Autor:        Stefan Duscher
#
# Bemerkung:    Ganz einfaches Beispiel
# ----------------------------------------------


# Bibliothek einbinden
import tkinter as tk 

# erzeuge ein Tk Objekt (Anzeigefenster) 
fenster = tk.Tk() 

# erzeuge ein Label-Widget (Anzeige im Fenster)
label = tk.Label (master=fenster, text="Hallo, wie gehts?") 

# starte den Layout Manager, positioniere label in Anzeigefenster mittels pack()
label.pack()

# zeige das Anzeigefenster am Bildschirm an
fenster.mainloop()
