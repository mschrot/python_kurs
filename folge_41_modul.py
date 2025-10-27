

# if __name__ == '__main__':
# wird in Python-Modulen oder -Dateien verwendet, um zu unterscheiden, ob die Datei direkt ausgeführt oder als Modul importiert wird.


def speed(gb, mbits):
    '''Geschwindigkeits berechnung'''  # help(speed)
    mb = gb * 1024
    mbps = mbits / 8
    wert = mb / mbps / 60  # in Minuten
    ausgabe = f'Die Downloadzeit für {gb} GB mit {mbits} Mbit/s beträgt {wert:.1f} Minuten.'
    return ausgabe


print(__name__)
if __name__ == '__main__':
    # DEMO TEST: speed
    print(speed(148, 100))
