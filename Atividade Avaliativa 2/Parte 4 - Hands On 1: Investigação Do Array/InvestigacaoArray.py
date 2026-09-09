# Atividade Avaliativa 2
# Parte 4 - Investigação do Array

temperaturas = []

print("Digite 10 temperaturas:")
for i in range(10):
    t = float(input(f"Temperatura {i}: "))
    temperaturas.append(t)

print("\nElementos armazenados:")
for i in range(10):
    print(f"Índice {i}: {temperaturas[i]}")

soma = temperaturas[0]
maior = temperaturas[0]
menor = temperaturas[0]
indice_maior = 0
indice_menor = 0

for i in range(1, 10):
    soma += temperaturas[i]
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i
    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i

media = soma / 10

acima_media = 0
for t in temperaturas:
    if t > media:
        acima_media += 1

print(f"\nMédia: {media:.2f}")
print(f"Maior valor: {maior} (Índice: {indice_maior})")
print(f"Menor valor: {menor} (Índice: {indice_menor})")
print(f"Valores acima da média: {acima_media}")
print("\nOperações de percurso: Foram necessários 2 percursos completos pelo array (20 acessos aos elementos no total).")
