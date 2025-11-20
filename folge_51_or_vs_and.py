# Prüfe, ob eine eingegebene Zahl zwischen 10 und 20 liegt.
zahl = 21

if zahl >= 10 and zahl <= 20:
    print('Zahl zwischen 10 und 20 liegt')


# Prüfe, ob jemand gratis ins Museum kommt:
# 		Unter 6 Jahren ✅
# 		Über 65 ✅
# 		Sonst ❌
# 		Aufgabe

old = 66

if old < 6 or old > 65:
    print('Gratis Museum ✅')
else:
    print('Volle Preis ❌')
