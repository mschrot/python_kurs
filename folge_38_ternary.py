# Der ternäre Operator in Python ist eingentlich eine Kurzschreibweise für if-else


wert = 5 > 3  # Python Ausdruck

ergebnis = 'wahr' if wert else 'falsch'
print(ergebnis)

print('True' if 5 > 3 else 'False')

# Ternäre Auswertung in eine Def (Funktion)


def ist_rener(old):
    return 'ja' if old >= 67 else 'nein'


print(ist_rener(68))

# Note Auswert

note = 1

if note == 1:
    print('Sehr Gut!')
elif note == 2:
    print('Gut!')
elif note <= 4:
    print('Bestanden!')
else:
    print('Nicht Bestanden!')


note = 4
ergebnis = 'Sehr Gut!' if note == 1 else 'Gut!' if note == 2 else 'Bestanden!' if note <= 4 else 'Nicht Bestande!'

print(ergebnis)
