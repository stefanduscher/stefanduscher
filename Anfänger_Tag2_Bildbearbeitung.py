# Programm:         Bearbeitung von Bilddateien
#
# Autor:            Stefan Duscher
#
# Datum:            26.09.2019
#
# Bemerkung:        Versionen der Bibliotheken werden
#                   angezeigt
#
# -----------------------------------------------------


# Bibliotheken importieren
import scipy as sp
import numpy as np
import imageio as im
import matplotlib as mpl
import matplotlib.pyplot as plt
import skimage as si


# Bilddaten Astronaut laden und in grau und negativ umwandeln
astronaut = si.color.rgb2gray(si.data.astronaut())
astronaut_farbe = si.data.astronaut()
astronaut_negativ = 255 - astronaut_farbe


# Bilddaten aus Bibliothek "misc.face" laden
tier = sp.misc.face()


# Bildbearbeitungsfunktion für Bild Astronaut
astronaut_rescaled = si.transform.rescale(astronaut, 0.50, anti_aliasing=False, multichannel = False)
astronaut_resized = si.transform.resize(astronaut_negativ, (astronaut.shape[0] // 4, astronaut.shape[1] // 4),
                       anti_aliasing=True)
astronaut_downscaled = si.transform.downscale_local_mean(astronaut, (4, 3))
astronaut_farbe_gedreht = si.transform.rotate(astronaut_farbe, 45, resize = True)


# Bilder speichern
im.imwrite("waschbaer_farbig.png", tier)
im.imwrite("waschbaer_grau.jpg", tier[:,:,0])
im.imwrite("astronaut.tif", astronaut_farbe)


# Stil der Fenster festlegen
plt.style.use("seaborn-white")  


# Fenster mit Bild von Waschbär erzeugen
plt.figure(1, figsize = (6,4))  # Fenstergröße beim Öffnen wird vorgegeben
plt.imshow(tier)
plt.title("Waschbär")


# Fenster mit mehreren Bildern erzeugen
fig, axes = plt.subplots(nrows=2, ncols=3, num = 2)

ax = axes.ravel() # Nimmt Inhalt von axes und ordnet sie in einer Zeile an

fig.set_size_inches(10,9)   # legt die Größe des Fensters beim Erzeugen fest

fig.suptitle("Darstellung von Bildern unter Python und Matplotlib", fontsize=20) # Gesamtüberschrift

# Subplot 1
ax[0].imshow(astronaut, cmap="gray")
ax[0].set_title("Original Foto")

# Subplot 2
ax[1].imshow(astronaut_rescaled, cmap="gray")
ax[1].set_title("Verkleinertes Bild ( mit Aliasing)")

# Subplot 3
ax[2].imshow(astronaut_resized)
ax[2].set_title("Verkleinertes Negativ (ohne Aliasing)")

# Subplot 4
ax[3].imshow(astronaut_downscaled, cmap="gray")
ax[3].set_title("Neues Seitenverhältnis (ohne Aliasing)")

# Subplot 5
ax[4].imshow(astronaut_farbe)
ax[4].set_title("Original Foto farbig")

# Subplot 6
ax[5].imshow(astronaut_farbe_gedreht)
ax[5].set_title("Foto gedreht (mit Ecken)")

# Festlegen der Achsen in Subplot 1
ax[0].set_xlim(0, 512)
ax[0].set_ylim(512, 0)

plt.tight_layout()  # Modus für ein "aufgeräumtes" Anordnen der Subplots
plt.show() # Anzeigen der erzeugten Grafik


# Ausgabe der Versionen der Pakete
print("Version Numpy:", np.__version__)
print("Version Scipy:", sp.__version__)
print("Version Matplotlib:", mpl.__version__)
print("Version Scikit:", si.__version__)
print("Version imageio:", im.__version__)

