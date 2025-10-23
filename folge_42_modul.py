# __________________________ 1 Funktion: speed

def speed(gb, mbits):
    '''Geschwindigkeits berechnung'''  # help(speed)
    mb = gb * 1024
    mbps = mbits / 8
    wert = mb / mbps / 60  # in Minuten
    ausgabe = f'Die Downloadzeit für {gb} GB mit {mbits} Mbit/s beträgt {wert:.1f} Minuten.'
    return ausgabe


# Ausgabetest: speed
if __name__ == '__main__':
    print(speed(80, 100))


# __________________________ 2 Funktion: ist_gerade_zahl

def ist_gerade_zahl(zahl):
    '''Ermitllung von gerade oder ungerade Zahl'''
    wert = 'gerade Zahl' if zahl % 2 == 0 else 'ungerade Zahl'
    ausgabe = f'Zahl {zahl} ist {wert}.'
    return ausgabe


# Ausgabetest: st_gerade_zahl
if __name__ == '__main__':
    print(ist_gerade_zahl(7))


# __________________________ 3 Funktion: bmi

def bmi(kg, m):
    '''BMI-Rechner: Body-Mass-Index berechnen'''
    bmi = kg / (m ** 2)
    if bmi < 18.5:
        print(f'BMI: {bmi:.1f} ist Untergewicht.')
    elif bmi <= 24.9:
        print(f'BMI: {bmi:.1f} ist Normalgewicht.')
    elif bmi <= 29.9:
        print(
            f'BMI: {bmi:.1f} ist Übergwicht.')
    else:
        print(f'BMI: {bmi:.1f} ist Fettleibigkeit.')


# Ausgabetest: bmi
if __name__ == '__main__':
    bmi(80, 1.85)

# __________________________ 4 Funktion: wurzel


def wurzel(zahl):
    '''Die Quadratwurzel einer Zahl zu ziehen'''
    wert = zahl ** (1/2)
    ausgabe = f'Die Quadratwurzel aus der Zahl {zahl} ist {wert:.2f}.'
    return ausgabe


# Ausgabetest: wurzel
if __name__ == '__main__':
    print(wurzel(7))
