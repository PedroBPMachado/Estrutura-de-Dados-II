import random
import sys 

sys.setrecursionlimit(10000) #Para evitar que o sistema interrompa a execução do quick sort em vetores grandes.

def bubble_sort(arr):
    comp = trocas = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    return comp, trocas

def insertion_sort(arr):
    comp = mov = 0
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        mov += 1 
        while j >= 0:
            comp += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                mov += 1  
                j -= 1
            else:
                break
        arr[j + 1] = chave
        mov += 1  
    return comp, mov

def selection_sort(arr):
    comp = trocas = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    return comp, trocas

def quick_sort(arr):
    def _quick(low, high):
        if low >= high:
            return 0, 0
            
        comp = mov = 0
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comp += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    mov += 1
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        mov += 1
        pivot_idx = i + 1
        
        c1, m1 = _quick(low, pivot_idx - 1)
        c2, m2 = _quick(pivot_idx + 1, high)
        
        return comp + c1 + c2, mov + m1 + m2

    return _quick(0, len(arr) - 1)


random.seed(42)
tamanhos = [10, 20, 1000]

print(f"{'Tam':<6} | {'Bubble (C / T)':<18} | {'Insertion (C / M)':<18} | {'Selection (C / T)':<18} | {'Quick (C / M)':<18}")
print("-" * 90)

for tam in tamanhos:
    original = [random.randint(1, 10000) for _ in range(tam)] #Vetor aleatório
    original = list(range(1, tam + 1)) #Vetor ordenado
    original = list(range(tam, 0, -1)) #Vetor inversamente ordenado

    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    b_c, b_t = bubble_sort(vetor_bubble)
    i_c, i_m = insertion_sort(vetor_insertion)
    s_c, s_t = selection_sort(vetor_selection)
    q_c, q_m = quick_sort(vetor_quick)
    
    print(f"{tam:<6} | {b_c:>7} / {b_t:<8} | {i_c:>7} / {i_m:<8} | {s_c:>7} / {s_t:<8} | {q_c:>7} / {q_m:<8}")

