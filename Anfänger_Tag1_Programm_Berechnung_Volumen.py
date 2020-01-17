# Programm:     Berechnung Volumen eines Quaders
#
# Autor:        Stefan Duscher
#
# Datum:        22.09.2019
#
# ---------------------------------------------------------------







def kubik(a,b,c):
    # Dieser Funktion werden drei Zahlen übergeben
    # sie multipliziert die drei Zahlen miteinander und gibt das Ergebnis zurück

    k = a*b*c
    return k




def eingabe():
    # Bitte achten Sie auf den float-Befehl: Hier wird als Typ eine Fließkommazahl (= Zahl mit Kommastellen / "Real-Zahl") zugewiesen

    l = float(input("Bitte Länge eingeben:"))
    b = float(input("Bitte Breite eingeben:"))
    h = float(input("Bitte Höhe eingeben:"))

    volumen = kubik(l,b,h)


    print("Das Volumen des Quaders beträgt mit drei Dezimalen: {0:.3f} Volumeneinheiten.".format(volumen))
    print("Dem Ergebnis ist aber nichts passiert. Die nächste Zeile zeigt es vollständig an.")
    print("Das Volumen des Quaders beträgt {0} Volumeneinheiten.".format(volumen))

    volumen = round(volumen, 2)

    print("Nun runden wir auf zwei Dezimalen. Das Ergebnis lautet: ", volumen)
    print("Nun haben wir die Zahl und nicht nur die Anzeige verändert.")

   

    return()


# Hauptprogramm



eingabe()







