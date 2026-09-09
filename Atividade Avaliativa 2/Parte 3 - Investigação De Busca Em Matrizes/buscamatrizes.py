# Atividade Avaliativa 2 
# Parte 3 - Investigação De Busca Em Matrizes

def buscar(matriz, valor):
    comp = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            comp += 1
            if matriz[i][j] == valor:
                return comp
    return comp

tamanhos = [2, 10, 100]

print(f"{'Matriz':<10} | {'Nº elementos':<12} | {'Início':<8} | {'Final':<8} | {'Inexistente':<11}")
print("-" * 62)

for n in tamanhos:
    matriz = []
    contador = 1
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(contador)
            contador += 1
        matriz.append(linha)
        
    total = n * n
    dimensao = f"{n}x{n}"
    inicio = buscar(matriz, matriz[0][0])
    final = buscar(matriz, matriz[n-1][n-1])
    inexistente = buscar(matriz, 99999)
    
    print(f"{dimensao:<10} | {total:<12} | {inicio:<8} | {final:<8} | {inexistente:<11}")
