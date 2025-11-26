# Fibonacci Algorithmus mit Python: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

import time

startzeit = time.time()
a = 0
b = 1

count = 0
while count <= 12:
    a, b = b, a + b
    print(f'Monat: {count} Hasenpopulation: {a}')
    count = count + 1

endzeit = time.time()
print('Programmlaufzeit beträgt:', endzeit - startzeit, 'in Sekunden!')
