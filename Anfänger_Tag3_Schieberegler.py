# Programm:     Interaktive Grafik mit Schieberegler
#
# Datum:        02. Juno 2019
#
# Autor:        Stefan Duscher
#
# Bemerkungen:  Kurs "Python für Anfänger" Ludwigsburg
#
# ----------------------------------------------------

# Einbinden der Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import Slider


# Abfrage der Eigenschaften der Bibliothek Matplotlib
def Abfragen_Matplotlib():
    mpl_version = mpl.__version__
    mpl_ort = mpl.__file__
    mpl_config = mpl.get_configdir()
    mpl_cache = mpl.get_cachedir()

    print("Version von Matplotlib:", mpl_version)
    print("Installationsort von Matplotlib:", mpl_ort)
    print("Die Konfigurationsinformationen befinden sich bei:", mpl_config)
    print("Der Zwischenspeicher / Cache befindet sich bei:", mpl_cache)
    



# Definition der x- und y-Werte
x = np.linspace(0,12,200)
y = np.sin(x)


bild = plt.figure()
# Hier wird "bild" zum Objekt figure(), das aus der Bibliothek Pyplot aus
# Matplotlib stammt. Diesem Objekt kann man später Eigenschaften zuweisen.

# Der eigentliche Plot und der Slider sollen übereinander stehen. 
# Mit einem einfachen 2x1-Raster werden sie aber gleich hoch.
# Wir erzeugen das Raster daher mit gridspec, da kann man ein 
# Höhenverhältnis angeben. 

gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[8, 1]) 
# Mit Gridspec unterteilt man vorbereitend ein Fenster, wenn man dann darin
# Subplots platzieren will. Details siehe den Link zur offiziellen Doku: 
# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.gridspec.GridSpec.html



zeichnen1 = bild.add_subplot(gs[0]) 
zeichnen2 = bild.add_subplot(gs[1])

# zeichnen1 und zeichnen2 sind ebenfalls Objekte; sie leiten sich aus dem Objekt
# Bild ab und geben ihm weitere Eigenschaften, nämlich dass eine Untergrafik ("Subplot")
# dem Bild zugewiesen wird. 
# zeichnen1 weist das Subplot gs[0] zu, das ist das obere 8 Neuntel hoche Subplot
# zeichnen2 weist das Subplot gs[1] zu, das ist das untere 1 Neuntel hohe Subplot



zeichnen1.plot(x,y)

# Der Slider füllt einen Subplot, hat einen Namen und Min-, Max- und Startwert
sl = Slider(zeichnen2, 'Frequenz ', 0.01, 5.0, valinit=1)
bild.show()

# Diese update-Funktion zeichnet den Graph neu:  
def myupdate(val):
    y = np.cos(val*x)           # val ist der am Schieberegler eingestellte Wert
    zeichnen1.cla()             # alten subplot löschen
    zeichnen1.plot(x,y)         # neu zeichnen
    bild.canvas.draw_idle()     # 


# Hier beginnt das Hauptprogramm

Abfragen_Matplotlib()

# hier wird dem Slider gesagt, dass er bei Änderungen die Funktion myupdate rufen soll    
sl.on_changed(myupdate)
