# Schaltjahr: / 4 ist, nicht durch 100 teilbar ist
# Wenn es durch 400 teilbar ist

jahr = 2008

while jahr <= 2025:

    # not bool(0): True and bool(1): True
    if not (jahr % 4) and (jahr % 100):
        print(f'Schaltjahr {jahr}')

    # bool(0): False
    elif not (jahr % 400):
        print(f'Schaltjahr {jahr}')
    jahr += 1
