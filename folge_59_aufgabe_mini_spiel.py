# 📘 Aufgaben: Erweitere deinen Code so, dass das Slot-Spiel immer wieder ausgeführt wird bis gewonnen steht:
# 📘 Estelle eine Gewinnquote: (1 / durchläufe) * 100
# z.B.:	--- Statistik ---
# Durchläufe bis zum Gewinn: 41
# Gewinnwahrscheinlichkeit: 2.44%

import random


emoji_kiste = ["🍒", "🍉", "⭐", "🍋", "💎"]

slot_1 = random.choice(emoji_kiste)
slot_2 = random.choice(emoji_kiste)
slot_3 = random.choice(emoji_kiste)

print(slot_1, slot_2, slot_3)


if slot_1 == slot_2 == slot_3:
    print('🎉 Gewonnen!')  # true
else:
    print('🙁 Verloren!')
