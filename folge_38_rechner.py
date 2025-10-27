# Aufgabe: Schreibe ein kleines Taschenrechner-Programm,
# das zwei Zahlen einliest, einen Rechenoperator (+, -, *, /) abfragt
# und anschließend das Ergebnis ausgibt.

zahl_1 = float(input('Erste Zahl: '))
op = input('+, -, *, / ')
zahl_2 = float(input('Zweite Zahl: '))

if op == '+':
    # print(zahl_1 + zahl_2)
    def summe(a, b):
        return a + b
    print(summe(zahl_1, zahl_2))
elif op == '-':
    print(zahl_1 - zahl_2)
elif op == '*':
    print(zahl_1 * zahl_2)
elif op == '/':
    print(zahl_1 / zahl_2)
else:
    print('Falsche Eingabe!')
