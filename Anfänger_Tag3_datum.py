# Programm:     datum.py
#
# Autor:        Stefan Duscher
#
# Datum:        04.06.2019
#
# ----------------------------------------

# Einbinden der Bibliotheken
import time

# Funktion, um einstelligen Zahlen als String eine Null voran zu stellen
def auffuellen(eingabe):
    """ Bekommt einen String übergeben und stellt ihm eine "0" voran, wenn er nur ein Zeichen lang ist. """
    
    if len(eingabe) == 1:
        eingabe = "0" + eingabe
    return eingabe


# Funktion zur Erzeugung der internationalen Zeitangabe als String
def zeitstempel():
    """ Gibt den aktuellen Zeitstempel im internationalen Format als String zurück. """

    heute = time.localtime()
    datum = str(heute.tm_year) + "-" + auffuellen(str(heute.tm_mon)) + "-" + auffuellen(str(heute.tm_mday))
    zeit = auffuellen(str(heute.tm_hour)) + ":" + auffuellen(str(heute.tm_min)) + ":" + auffuellen(str(heute.tm_sec))
    zeitangabe = datum + "  " + zeit
    return zeitangabe

# Hauptprogramm
print("Die aktuelle Zeitangabe lautet:" + zeitstempel() )
