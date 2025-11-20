def datum(*, tag: int, monat: str) -> str:
    return f'Heute ist {tag} {monat}.'


print(datum(tag=20, monat='November'))


# Funktion 2
def hallo(*, name: str, gruss='Hallo,') -> str:
    return f'{gruss} {name}'


print(hallo(name='Max'))
