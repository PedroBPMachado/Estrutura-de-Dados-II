# Atividade Avaliativa 2:
# Parte 2 - Experimento de Ordenação

import random

def bubble_sort(vetor):
    comparacoes = 0
    trocas = 0
    n = len(vetor)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocas += 1
                trocou = True
        if not trocou:
            break
    return comparacoes, trocas

def quick_sort(vetor):
    comparacoes = [0]
    movimentacoes = [0]
    
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            comparacoes[0] += 1
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                movimentacoes[0] += 1
        items[i + 1], items[high] = items[high], items[i + 1]
        movimentacoes[0] += 1
        return i + 1

    _quick_sort(vetor, 0, len(vetor) - 1)
    return comparacoes[0], movimentacoes[0]

if __name__ == "__main__":
    tamanhos = [10, 20, 1000]
    print(f"{'Tamanho':<10} | {'Bubble Comp':<12} | {'Bubble Trocas':<13} | {'Quick Comp':<11} | {'Quick Mov':<10}")
    print("-" * 65)

    for tam in tamanhos:
        original = [random.randint(1, 10000) for _ in range(tam)]
        
        c1 = original.copy()
        b_comp, b_trocas = bubble_sort(c1)
        
        c2 = original.copy()
        q_comp, q_mov = quick_sort(c2)
        
        print(f"{tam:<10} | {b_comp:<12} | {b_trocas:<13} | {q_comp:<11} | {q_mov:<10}")
