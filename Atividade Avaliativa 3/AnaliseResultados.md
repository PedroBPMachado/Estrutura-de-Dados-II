## Tabela de Resultados do Experimento

Resultados exatos obtidos a partir da execução do algoritmo.

| Tamanho ($N$) | Bubble (Comp / Trocas) | Insertion (Comp / Mov) | Selection (Comp / Trocas) | Quick (Comp / Mov) |
| :---: | :---: | :---: | :---: | :---: |
| **10** | 45 / 19 | 27 / 37 | 45 / 7 | 29 / 8 |
| **20** | 190 / 84 | 99 / 122 | 190 / 16 | 58 / 30 |
| **1.000** | 499.500 / 239.681 | 240.670 / 241.679 | 499.500 / 992 | 10.385 / 4.718 |

*Legenda: **Comp** = Comparações | **Trocas** = Trocas diretas | **Mov** = Movimentações de elementos.*

---

## Etapa 4 – Análise dos Resultados

### a) Qual algoritmo realizou o menor número de comparações para 10 elementos?
O **Insertion Sort**, que realizou apenas **27 comparações**. Isso ocorre porque o algoritmo interrompe o laço de verificação interno assim que encontra a posição correta do elemento no subvetor já ordenado, sem precisar percorrer os demais elementos.

### b) Qual algoritmo realizou menos trocas ou movimentações?
O **Selection Sort**, realizando apenas **7 trocas** para $N=10$, **16 trocas** para $N=20$ e **992 trocas** para $N=1000$. Ele varre a lista procurando o menor valor e executa no máximo uma troca por iteração do laço externo.

### c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?
Sim. A relação proporcional se manteve: para os algoritmos de complexidade quadrática ($O(N^2)$), dobrar o tamanho do vetor de 10 para 20 elementos quadruplicou a quantidade de comparações no Bubble Sort e Selection Sort. O Quick Sort acompanhou esse crescimento de forma muito mais moderada (de 29 para 58 comparações).

### d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?
Ocorreu uma divergência drástica no desempenho:
* Os algoritmos $O(N^2)$ sofreram uma explosão operacional. O Bubble e o Selection Sort atingiram **499.500 comparações**, e o Insertion Sort atingiu **241.679 movimentações**.
* O **Quick Sort** manteve um crescimento controlado por sua natureza $O(N \log N)$, realizando apenas **10.385 comparações** e **4.718 movimentações**.

### e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade $O(N^2)$ em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações? Explique utilizando seus resultados.
Não apresentaram a mesma quantidade de operações. Constantes e termos de menor ordem podem alterar o resultado para diferentes sorts:
* **Selection Sort:** Realizou o número fixo e máximo de comparações ($\frac{N(N-1)}{2} = 499.500$ para $N=1.000$), mas teve um número baixíssimo de trocas (992).
* **Bubble Sort:** Teve as mesmas 499.500 comparações do Selection, mas acompanhadas de um número massivo de trocas (239.681).
* **Insertion Sort:** Realizou aproximadamente a metade das comparações em relação ao Bubble e Selection (240.670 comparações para $N=1.000$), pois interrompe a busca interna precocemente.

### f) Qual algoritmo apresentou maior crescimento no número de operações?
O **Bubble Sort**, pois além de executar a quantidade máxima de comparações quadráticas, realiza trocas a cada par fora de ordem encontrado, resultando no maior volume acumulado de operações.

### g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?
O Quick Sort apresentou uma taxa de crescimento $O(N \log N)$. Para $N=1.000$, o que resulta na quantidade de comparações sendo muito inferior a do Bubble Sort e o Selection Sort, demonstrando uma eficiência significativamente superior.

### h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?
Sim. O experimento comprovou na prática que algoritmos de divisão e conquista de ordem $O(N \log N)$ superam exponencialmente os algoritmos elementares $O(N^2)$ quando a escala dos dados aumenta.

### i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria? Justifique utilizando os resultados do experimento.
Escolheria o **Quick Sort**. Os resultados para $N=1.000$ provam que ele exige uma fração mínima do esforço computacional dos demais algoritmos, garantindo o menor tempo de resposta e maior escalabilidade para a central de distribuição.

---

## Desafio Adicional

A organização inicial dos dados **não afeta todos os algoritmos da mesma maneira, usaremos 20 elementos para demonstrar:**:

## Vetor Aleatório

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 190 | 84 |
| Insertion Sort | 99 | 122 |
| Selection Sort | 190 | 16 |
| Quick Sort | 58 | 30 |

* Como podemos observar, utilizando um vetor aleatório, o **Quick Sort** foi quem menos precisou fazer comparações e trocas, graças a sua natureza $O(N \log N)$.

## Vetor Ordenado

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 190 | 0 |
| Insertion Sort | 19 | 38 |
| Selection Sort | 190 | 0 |
| Quick Sort | 190 | 19 |

* Agora, com um vetor já ordenado, podemos observar que o **Quick Sort** perde a sua eficiência, precisando do máximo de trocas e movimentações possíveis, isso ocorre devido as partições extremamente desequilibradas geradas pelo vetor completamente organizado.

* # Vetor Inversamente Ordenado

|  Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 190 | 190 |
| Insertion Sort | 190 | 228 |
| Selection Sort | 190 | 10 |
| Quick Sort | 190 | 19 |

* Com o algoritmo dessa vez usando um vetor inversamente ordenado, podemos observar que, dessa vez, a maioria dos sorts não conseguiram desempenhar bem, a escolha ruim do pivô continuou afetando o **Quick Sort**, e a ordem, que agora desfavorece o **Bubble Sort** resultou em um aumento explosivo das suas trocas.
