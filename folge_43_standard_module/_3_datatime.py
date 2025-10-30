# 3. datetime – Mit Datum und Zeit arbeiten
from datetime import datetime

jetzt = datetime.now()

print(f'Aktuelle Datume und Uhrzeit: {jetzt}')
print(f'Aktuelle Monat: {jetzt.month}')
print(f'Aktuelle Jahr: {jetzt.year}')
