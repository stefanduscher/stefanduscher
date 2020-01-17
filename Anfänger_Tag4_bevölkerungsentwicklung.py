# Datei:        Einlesen einer csv-Datei
#
# Datum:        11.06.2019
#
# Autor:        Stefan Duscher
#
# Bemerkung:    Eingelesen wird die Bevölkerungsentwicklung von Kiel
#
#
# ----------------------------------------------------------------


# Importieren der notwendigen Bibliotheken
import matplotlib.pyplot as plt
import csv


# Funktion zum Unwandeln einer Liste in String
def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return(str_list)


# --  Hauptprogramm  --

# Definition der Grafik als Objekt
fig = plt.figure('Titel des Fensters', figsize = [8, 6])


# Einlesen der csv-Datei
with open('data/kiel_bevoelkerung_familienstand.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    
    # create empty lists
    jahr = []
    ledig = []
    verheiratet = []
    
    for row in readCSV:
        
        a = row[4]
        b = row[5]
        c = row[6]
        
        jahr.append(a)
        ledig.append(b)
        verheiratet.append(c)
        

# Entfernen des ersten Elementes der eingelesenen Spalten
jahr.remove("Jahr")
ledig.remove("ledig")
verheiratet.remove("verheiratet")



# Umwandeln der Elemente in einer Liste zum Typ Integer
jahr_zahl = str_list_to_int_list(jahr)
ledig_zahl = str_list_to_int_list(ledig)
verheiratet_zahl = str_list_to_int_list(verheiratet)

# Titel der Grafik
plt.title("Kiel - Familienstand", size="x-large")

# Beschriftung der Y-Achse
plt.ylabel("Einwohner", size="x-large")

# Beschriftung der X-Achse
plt.xlabel("Jahr", size="x-large")

# Ausgabe der Grafik
plt.plot(jahr_zahl, ledig_zahl, "r*-", markersize=6, linewidth=1, color='g', label="ledig")
plt.plot(jahr_zahl, verheiratet_zahl, "r*-", markersize=6, linewidth=1, color='r', label="verheiratet")

# Festlegung der Legende
plt.legend(loc="upper left")

# Anzeigen des erzeugten Grafikobjekts
plt.show()
