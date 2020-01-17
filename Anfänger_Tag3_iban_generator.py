# Programm:     IBAN-Code-Generator
#
# Autor:        Stefan Duscher
#
# Datum:        30.06.2019
#
# -------------------------------------
#


def eingabe_blz():
    # Eingabe der Bankleitzahl; dabei prüfen, dass die
    # Bankleitzahl aus 8 Stellen besteht
    eingabe = ""
    while (len(eingabe) != 8):
        eingabe = input("Bitte Bankleitzahl eingeben:")
        if (len(eingabe) != 8):
            print("\n")
            print("Die Bankleitzahl muss aus acht Stellen bestehen. \n")
    eingabestr = str(eingabe)
    return eingabestr


def eingabe_kontonummer():
    # Eingabe der Kontonummer; dabei prüfen, dass die
    # Kontonummer aus 10 Stellen besteht
    eingabe = ""
    while (len(eingabe) != 10):
        eingabe = input("Bitte Kontonummer eingeben:")
        if (len(eingabe) != 10):
            print("\n")
            print("Die Kontonummer muss aus zehn Stellen bestehen. \n")
    eingabestr = str(eingabe)
    return eingabestr


def checksumme_iban(nummer):
    # Berechnung der Prüfzimmer, indem die Nummer module 97
    # gerechnet wird. Ggf. wird eine Null vorangestellt.
    # Rückgabetyp ist String.
    checksum = 98 - (nummer % 97)
    if (checksum < 10):
        checksumstr = "0" + str(checksum)
    else:
        checksumstr = str(checksum)
    return checksumstr


def erzeuge_iban(kontonummer, blz):
    # Funktion zur Erzeugung der IBAN. Kontonummer und
    # Bankleitzahl werden als String übergeben, das
    # Ergebnis kommt ebenfalls als String zurück
    lange_nummer = int(blz + kontonummer + "131400")
    checksum = checksumme_iban(lange_nummer)
    iban = "DE" + str(checksum) + str(blz) + str(kontonummer)
    return iban


# Hauptprogramm

blz = eingabe_blz()
konto = eingabe_kontonummer()

print("Der IBAN-Code lautet:", erzeuge_iban(konto,blz))


                        


        
    
