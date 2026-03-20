# Lotto Generator: 6 Zahlen aus 1 - 49 und ein Superzahl (0–9)

from random import sample, randint

lottozahl = list(sample(range(1, 50), 3))
print('Lottozahl', lottozahl)

superzahl = randint(0, 9)
print('Superzahl', superzahl)
