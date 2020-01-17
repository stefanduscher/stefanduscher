# Programm:     Verschlüsselung einer Zeichenfolge nach Caesar
#
# Autor:        Stefan Duscher
#
# Datum:        29.05.2019 und 04.10.2019
#
# ---------------------------------------------------------------


# Funktion zum Verschlüsseln
def verschluesseln(s, n):
    L = []
    for x in s:
        if x.isalpha():
            if 65 <= ord(x) <= 90:    # Grossbuchstabe
                L.append(chr(((ord(x) - 65 + n) % 26) + 65))
            if 97 <= ord(x) <= 122:   # Kleinbuchstabe
                L.append(chr(((ord(x) - 97 + n) % 26) + 97))
        else:
            L.append(x) # x ist keine Buchstabe, wird unverändert angehängt        
    return "".join(L)   # Verschmelzen der einzelnen Buchstaben zu einem String


# Funktion zum Entschlüsseln
def entschluesseln(s, n):
    return verschluesseln(s, -n)
    
    
def main():
    print("Bitte Zeichenkette eingeben:")
    s = input()
    n = -1
    while n < 0 or n > 26:
        n = int(input("Bitte Schlüssel eingeben (natürliche Zahl zwischen 0 und 26): "))
    print()
    krypto = verschluesseln(s, n)
    print("Verschlüsselte Nachricht:\n", krypto)
    klartext = entschluesseln(krypto, n)
    print("Entschlüsselte Nachricht:\n", klartext)
    
main()    
