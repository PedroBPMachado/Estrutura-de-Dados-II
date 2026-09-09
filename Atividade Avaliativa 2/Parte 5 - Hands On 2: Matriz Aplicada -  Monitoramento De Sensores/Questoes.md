# Análise das Questões

* **a) Por que são necessários loops aninhados?**

```
Porque a estrutura é bidimensional (matriz). O loop externo é necessário para percorrer as linhas (os sensores) e o loop interno percorre as colunas (os horários) de cada linha, permitindo acessar todos os dados organizados em duas dimensões.

```

* **b) Qual o papel dos índices [i][j]?**

```
O índice i indica a linha atual (o sensor específico, de 0 a 4) e o índice j indica a coluna atual (o horário da medição, de 0 a 23). Juntos, eles localizam e permitem manipular exatamente cada elemento armazenado na matriz.

```

* **c) Quantas posições da matriz são percorridas?**

```
Em cada percurso completo, são percorridas exatamente 120 posições, correspondendo ao total de elementos da matriz (5 linhas multiplicadas por 24 colunas).

```

* **d) Qual a relação entre o número de linhas, colunas e quantidade de operações?**

```
A quantidade de operações em um percurso completo é o produto entre o número de linhas e o número de colunas. Se as dimensões da matriz aumentarem, o número de operações cresce diretamente na proporção desse produto.

```

---
