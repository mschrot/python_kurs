
# Ein Drache bekommt bis 100 Jahre drei Köpfe pro Jahr, danach zwei, berechne für Alter N seine Kopf- und Augenzahl.

def drache(*, jahr: int) -> int:
    '''Drachen Funkion'''
    if jahr <= 100:
        k = 1 + (jahr * 3)
    else:
        k = 1 + (100 * 3) + (jahr - 100) * 2

    a = k * 2
    return k, a  # lokale variablen


j = 107
k, a = drache(jahr=j)  # einzelwerten aus tuple auspacken in variable

print(f'Drachen ist {j} Jahre alt und hat {k} Köpfe und {a} Augen.')
