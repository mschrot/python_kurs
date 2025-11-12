# ✅ 10. Eingabe validieren
# Fordere den Benutzer auf, eine Zahl zwischen 10 und 20 einzugeben. Solange er etwas anderes schreibt, frag erneut.



# if (zahl >= 10) and (zahl <= 20):
# if zahl >= 10 and zahl <= 20:
# if zahl >= 10 or zahl <= 20: # falschen verwendung von or 
# if 10 <= zahl and zahl <= 20:

while True:
    zahl = int(input('Zahl eingeben zw. 10 & 20: '))
    if 10 <= zahl <= 20:
        print('Korrekt Eingabe!')
        break

