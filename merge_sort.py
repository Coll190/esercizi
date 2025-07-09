import time
start = time.time()
def merge_sort(vet):
    if len(vet) > 1:
        left_vet = vet[:len(vet)//2]
        right_vet = vet[len(vet)//2:]

        merge_sort(left_vet)
        merge_sort(right_vet)
        
        i = 0
        j = 0
        k = 0

        while i < len(left_vet) and j < len(right_vet):
            if left_vet[i] < right_vet[j]:
                vet[k] = left_vet[i]
                i += 1
            else:
                vet[k] = right_vet[j]
                j += 1
            
            k += 1
        
        while i < len(left_vet):
            vet[k] = left_vet[i]
            i += 1
            k += 1
        
        while j < len(right_vet):
            vet[k] = right_vet[j]
            j += 1
            k += 1

vet = [2,6,5,1,7,4,3,4,4,4,4,6,7,1,0,8,4]
print("prima dell'ordinamento:")
print(vet)
merge_sort(vet)
print("dopo l'ordinamento:")
print(vet)
end = time.time()
print(f"tempo impiegato: {end - start:.6f} secondi")


