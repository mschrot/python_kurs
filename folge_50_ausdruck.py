# ✅ Ein Python-Ausdruck liefert immer einen Wert

ausdruck = 'Hallo World!'
obj_class = type(ausdruck)
obj_elements = len(ausdruck)
obj_id = id(ausdruck)
boolean = 'True: 1' if ausdruck else 'False: 0'
all_methoden = dir(ausdruck)

print(f'Wert: {ausdruck}')
print(f'Datentyp: {obj_class}')
print(f'Wie viel Elements: {obj_elements}')
print(f'Boolean-Wert: {boolean}')
print(f'ID von Obj: {obj_id}')
# print(f'Alle Methoden für diesen Objekt: {all_methoden}')
