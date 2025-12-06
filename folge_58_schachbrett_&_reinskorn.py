# 1️⃣ Standard-Güterwaggons: 60 Tonnen Reis:
# 60.000 kg × 50.000 Körner/kg ≈ 3.000.000.000.000 Körner


feld = 1

while feld <= 64:
    reis = 2 ** (feld - 1)
    print(f'Feld: {feld} Reiskörner: {reis / 3000000000000:,.0f}')
    feld += 1
