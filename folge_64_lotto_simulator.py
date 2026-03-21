# Lotto Generator: 6 Zahlen aus 1 - 49 und ein Superzahl (0–9)

from random import sample, randint
import time

anzahl = 2

lottozahl = sorted(sample(range(1, 50), anzahl))
superzahl = randint(0, 9)
lottozahl.append(superzahl)
print(lottozahl)


versuche = 0

startzeit = time.time()
while True:
    versuche += 1
    zufall_zahl = sorted(sample(range(1, 50), anzahl))
    super_zahl = randint(0, 9)
    zufall_zahl.append(super_zahl)
    print(zufall_zahl)

    if lottozahl == zufall_zahl:
        print(f'\n🎉 Gewonne!')
        print(f'🎲{lottozahl} : {zufall_zahl}')
        print(f'🍀 Versuche: {versuche}')
        break

endzeit = time.time()
print(f'⏰ {(endzeit - startzeit) / 60:.4f} Minuten \n')
