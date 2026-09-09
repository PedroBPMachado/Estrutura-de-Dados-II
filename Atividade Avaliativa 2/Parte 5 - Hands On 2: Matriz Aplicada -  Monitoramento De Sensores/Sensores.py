# Atividade Avaliativa 2
# Parte 5 - Sensores

import random

sensores = []
for i in range(5):
    linha = []
    for j in range(24):
        linha.append(round(random.uniform(15.0, 35.0), 1))
    sensores.append(linha)

soma_geral = 0
total_leituras = 5 * 24

maior_temp = sensores[0][0]
sensor_maior = 0
horario_maior = 0

print("--- Média de cada sensor ---")
for i in range(5):
    soma_sensor = 0
    for j in range(24):
        val = sensores[i][j]
        soma_sensor += val
        soma_geral += val
        
        if val > maior_temp:
            maior_temp = val
            sensor_maior = i
            horario_maior = j
            
    media_sensor = soma_sensor / 24
    print(f"Sensor {i}: {media_sensor:.2f} °C")


media_geral = soma_geral / total_leituras
print(f"\nMédia geral: {media_geral:.2f} °C")
print(f"\nMaior temperatura registrada: {maior_temp} °C")
print(f"Sensor responsável: Sensor {sensor_maior}")
print(f"Horário da ocorrência: {horario_maior}h")


limite = float(input("\nInforme um limite de temperatura (°C): "))
acima_limite = 0

for i in range(5):
    for j in range(24):
        if sensores[i][j] > limite:
            acima_limite += 1

print(f"Quantidade de leituras acima do limite: {acima_limite}")
