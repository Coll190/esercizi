f = open("index.txt")

testo = f.read()
testo = testo.lower()
lista = testo.split()

print(lista)
print(testo)

dizionario = {}
bh = "abcdefghijklmnopqrstuvwxyz"

for i in bh:
    ris = [parola for parola in lista if i in parola]
    print(f"parole che contengono '{i}': {ris}")
    print()

    dizionario[i] = ris

print("Dizionario finale")

for i, parole_set in dizionario.items():
    print(f"{i}: {parole_set}")
