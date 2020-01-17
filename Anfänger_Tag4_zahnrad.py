# Programm:     zahnrad.py
#
# Autor:        Stefan Duscher
#
# Datum:        25.01.2018
#
# Inhalt:       Zwei sich drehende Zahnräder
#
# ------------------------------------------------------

# Importieren der Bibliotheken
import numpy as np              # Gibt den Funktionen aus numpy das Suffix "np"
import matplotlib.pyplot as plt # Gibt den Funktionen aus der Bibliothek
                                # matplotlib.pyplot das Suffix "plt"
from matplotlib.patches import Polygon      # Import der Teilbibliothek "Polygon"
import matplotlib.animation as animation    # Import der Befehle für Animationen
                                            # aus der Bibliothek Matplotlib




def createGear(r, anzahl_zaehne, hoehe_zaehne):
    # r :               Zahnradradius
    # anzahl_zaehne :   Anzahl der Zähne eines Zahnrades
    # hoehe_zaehne :    Höhe der Zähne

    d_phi = 2*np.pi/anzahl_zaehne   # Unterteilung des Vollkreises
                                    # dividiert durch die Anzahl der Zähne
    tooth_points_angle = np.array([-1./3,-1./6,1./6,1./3])*d_phi    # Definition der Winkel der 4 Eckpunkte
                                                                    # im Bogenmaß
    tooth_point_r      = np.array([r-hoehe_zaehne/2., r+hoehe_zaehne/2., 
                                   r+hoehe_zaehne/2., r-hoehe_zaehne/2.])   # Definition der Abstände der
                                                                            # der 4 Punkte vom Mittelpunkt
                                                                            # Damit Polarkoordinaten erzeugt
    tooth =  tooth_point_r * np.exp(1j*tooth_points_angle)  # Enthält die Koordinaten der Zähne in
                                                            # komplexen Zahlen

    
    return np.outer(np.exp(1j*d_phi*np.arange(anzahl_zaehne)), tooth).flatten()     # Führe das äußere Vektorprodukt
                                                                                    # durch (outer) und mache daraus
                                                                                    # einen Vektor (flatten)
                                                                                    # Das sind die Koordinaten aller
                                                                                    # Eckpunkte aller Zähne
                                            



g1 = createGear(r=8, anzahl_zaehne=32, hoehe_zaehne=1)
g2 = createGear(r=4, anzahl_zaehne=16, hoehe_zaehne=1)

g2 *= np.exp(1j*2*np.pi/32)
d2 = 12

stepCount=12 # Aufteilung der Bewegung in 12 Abschnitte / Frames
step = 2*np.pi/32/stepCount # Schrittweite Drehung des großen Zahnrades

fig = plt.figure(figsize=(3,2))
ax = fig.add_axes([-.05, -.05, 1.1, 1.1])
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_aspect("equal")
plt.margins(0,0)
plt.xlim(-9.5,17.6)
plt.ylim(-9.5,9.5)

ims = []
for i in range(stepCount):
    g1 *= np.exp( 1j*step)
    g2 *= np.exp(-2j*step)
    ims.append([ax.add_patch(Polygon(g1.view(float).reshape(g1.size,2),
                                     color=(.1,0,1,.5))),
                ax.add_patch(Polygon(g2.view(float).reshape(g2.size,2)+[d2,0],
                                     color=(1,0,.1,.5)))])


ani = animation.ArtistAnimation(fig, ims, interval=1000. * 2/3 / stepCount)

plt.show()
