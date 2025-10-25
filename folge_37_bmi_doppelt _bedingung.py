# Formel: (Erwachsene, WHO)
# BMI = Gewicht (kg) / (Größe (m) * Größe (m))
# Untergewicht: BMI < 18,5
# Normalgewicht: BMI 18,5 - 24,9
# Übergewicht: BMI 25 - 29,9
# Adipositas (Fettleibigkeit): BMI >= 30


kg = 60
m = 1.9
bmi = kg / (m ** 2)

if bmi < 18.5:
    if bmi >= 17:
        print(f'BMI ist {bmi:.2f}: leichtes Untergewicht!')
    elif bmi >= 16:
        print(f'BMI ist {bmi:.2f}: mäßiges Untergewicht!')
    else:
        print(f'BMI ist {bmi:.2f}: starkes Untergewicht!')

elif bmi <= 24.9:
    print(f'BMI ist {bmi:.2f}: Normalgewicht!')
elif bmi <= 29.9:
    print(f'BMI ist {bmi:.2f}: Übergewicht!')
else:
    print(f'BMI ist {bmi:.2f}: Adipositas!')


# Untergewicht	< 18.5
    # 17 - 18,5 leichtes Untergewicht
    # 16 - 16,9 mäßiges Untergewicht
    # < 16 starkes Untergewicht

# Normalgewicht	18.5 – 24.9
# Übergewicht	25 – 29.9

# Adipositas Grad I	30 – 34.9
    # Adipositas Grad II	35 – 39.9
    # Adipositas Grad III	≥ 40
