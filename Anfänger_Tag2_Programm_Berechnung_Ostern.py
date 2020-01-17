# Programm zur Ostertag-Berechnung
#
# Autor: Stefan Duscher
#
# Datum: 28.09.2019
#
# ---------------------------------------------------------------


# ---- Funktion, damit nur Jahreszahlen eingegeben werden können
# ---- Funktion bekommt nichts übergeben, sie gibt eine eingegebene Jahreszahl zurück
#
def eingabe_jahr():
    while True:
        eingabe = input("Bitte das Jahr (ab 1583) eingeben:")
        try:
            jahres_eingabe = int(eingabe)
        except ValueError:
            print("Ungültige Eingabe")
        else:
            break
    jahr_eingabe = int(eingabe)
    return jahr_eingabe


# ---- Funktion, um das Osterdatum zu berechnen
# ---- Sie bekommt eine Jahreszahl übergeben
# ---- Sie gibt einen Array / Vektor mit zwei Elementen (Tag, Monat) zurück

def berechne_ostern(jahr):
    a = jahr % 19
    print("a hat den Wert ",a)
    b = jahr // 100
    print("b hat den Wert ",b)
    c = jahr % 100
    print("c hat den Wert ",c)
    d = b // 4
    print("d hat den Wert ",d)
    e = b % 4
    print("e hat den Wert ",e)
    f = (b + 8) // 25
    print("f hat den Wert ",f)
    g = (b - f + 1) // 3 
    print("g hat den Wert",g)
    h = ((19 * a) + b + 15 - d - g) % 30
    print("h hat den Wert ",h)
    i = c // 4
    print("i hat den Wert ",i)
    j = c % 4
    print("j hat den Wert ",j)
    k = (2 * (e + i) + 32 - h - j) % 7
    print("k hat den Wert ",k)
    l = ((((2 * k) + h) * 11) + a) // 451
    print("l hat den Wert ",l)
    m = ((h + k + 114) - (7 * l)) // 31
    print("m hat den Wert ",m) # m enthält den Monat
    n = ((h + k + 114) - (7 * l)) % 31
    n = n + 1 # n enthält den Tag
    print("n hat den Wert ",n)
    return m,n


# ---- Funktion, um die Ergebnisse auszugeben
# ---- An die Funktion wird ein Datum als 2-stelliges Array übergeben
# ---- Die Funktion gibt nichts mit Return zurück, sondern gibt Ergebnis auf Bildschirm aus
#
def ostern_ausgabe(osterdatum):
    monat_ostern_zahl = osterdatum[0]
    tag_ostern_zahl = osterdatum[1]
    monate = ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
    monat_ostern_name = monate[monat_ostern_zahl - 1]
    print("Das gesuchte Osterdatun lautet ",tag_ostern_zahl,".",monat_ostern_name)



# ------- Hauptprogramm

# ---- Schleife für die Eingabe der Jahreszahl
# ---- Solange Eingabe kleiner als 1583, solange wird Eingabefunktion aufgerufen

jahreszahl = 0  # Jahreszahl auf Null setzen, damit Schleife mindestens einmal durchlaufen wird
while (jahreszahl < 1583):
    jahreszahl = eingabe_jahr()

# ---- Aufruf, um Ostern zu berechnen
ostern = berechne_ostern(jahreszahl)

# ---- Aufruf, um die Ergebnisse auszugeben
ostern_ausgabe(ostern)


