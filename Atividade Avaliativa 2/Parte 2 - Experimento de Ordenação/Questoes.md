# Análise das Questões
* **a) Qual algoritmo realizou menos operações para 10 elementos?**
```
O Quick Sort realizou menos operações (comparações e movimentações somadas) do que o Bubble Sort,
embora para arrays tão pequenos a diferença absoluta seja pequena.
```
* **b) O comportamento permaneceu igual para 20 elementos?**
```
Sim, a proporção se manteve e a diferença começou a se acentuar. O Bubble Sort apresentou um crescimento mais acelerado
nas contagens de comparações e trocas em comparação ao Quick Sort.
```
* **c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?**
```
Houve uma discrepância drástica. O Bubble Sort exigiu centenas de milhares de operações
enquanto o Quick Sort processou os 1.000 elementos com apenas cerca de dez mil operações.
```
* **d) Qual algoritmo apresentou maior crescimento da quantidade de operações?**
```
O Bubble Sort, cujo número de operações cresce de forma quadrática em relação ao tamanho da entrada.
```
* **e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?**
```markdown
 Perfeitamente. Os dados refletem a curva teórica para o Bubble Sort:

$$O(n^2)$$

E para o Quick Sort:

$$O(n \log n)$$
```
* **f) Em qual situação você escolheria Bubble Sort?** 
```
  Apenas em cenários educacionais para ensino de lógica ou quando o array for extremamente pequeno
 (ex: menos de 10 elementos) e a facilidade de escrita imediata se sobreponha a qualquer requisito de performance.
```
* **g) Em qual situação você escolheria Quick Sort?**
```
Em cenários gerais de processamento de dados que exigem alto desempenho
```

---
