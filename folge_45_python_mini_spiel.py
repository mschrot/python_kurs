# 📝 Aufgabenstellung

# Programmiere in Python ein kleines Glücksspiel mit Emojis.
# Das Programm soll zufällig drei Emojis aus einer Liste auswählen und anzeigen.
# ["🍒", "🍉", "⭐", "🍋", "💎"]
# Sind alle drei Emojis gleich, soll eine Gewinnmeldung ausgegeben werden: 🎉 Gewonnen!
# Sind sie unterschiedlich, erscheint: 🙁 Verloren!
# Nutze dafür das Modul random.

# 1.) modul import
import random

# 2.) Obj mit viele...
emoji_kiste = ["🍒", "🍉", "⭐", "🍋", "💎"]  # Liste

# 3.) Objk. aus eine Kiste zufällig ziehen mit randomo fnk.

slot_1 = random.choice(emoji_kiste)
slot_2 = random.choice(emoji_kiste)
slot_3 = random.choice(emoji_kiste)

# 4 Zufällige Obj. Ausgeben
print(slot_1, slot_2, slot_3)

# 5 If Bedingung
if slot_1 == slot_2 == slot_3:
    print('🎉 Gewonnen!')  # true
else:
    print('🙁 Verloren!')

