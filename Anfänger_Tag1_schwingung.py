# Programmfunktion: Zeichnet einen Funktionsgraphen
#
# Autor: Stefan Duscher
#
# Datum: 03.07.2014
#
# ------------------------------------------------
#
# Importieren der Bibliotheken
import matplotlib.pyplot as plt
import numpy as npy

# Erzeugung eines Vektors mit Werten 0.0 bis 12.5 mit Abstand 0.1
t = npy.arange(0.0 , 12.6 , 0.1)
# Erzeugung eines Vektors y mit y = f(t)
y = 5*npy.sin(t)*npy.exp(-0.1*t)
# Erzeugung eines Vektors z mit z = f(t)
z = 5*npy.cos(t)*npy.exp(-0.2*t)
# Ausdruck der Funktionen y und z über t, y mit Linie, z mit Kreuzen
plt.plot(t,y,"-",t,z,"+",linewidth = 2)
# Beschriftung der Achsen
plt.xlabel('Zeit in Sekunden')
plt.ylabel('y(t)')
# Überschrift
plt.title('Dämpfungsfunktion')
# Anzeige eines Gitters in der Zeichenfläche
plt.grid(True)
# Anzeigen der Zeichnung
plt.show()
