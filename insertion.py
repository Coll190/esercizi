import time

vet = [2,6,5,1,3,4]

print("prima dell'ordinamento:")
print(vet)
print("dopo l'ordinamento:")

start = time.time()

for i in range(1,len(vet)):
    j = i
    while vet[j - 1] > vet[j] and j > 0:
        vet[j - 1], vet[j] = vet[j], vet[j - 1]
        j -=1

end = time.time()

print(vet)
print(f"tempo impiegato: {end - start:.6f} secondi")