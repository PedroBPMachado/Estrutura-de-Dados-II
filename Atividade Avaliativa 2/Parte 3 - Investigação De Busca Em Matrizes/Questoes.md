# Análise das Questões

* **a) Por que encontrar um elemento no início exige menos operações?**

```
Porque a busca sequencial percorre a matriz elemento por elemento, linha por linha, a partir da primeira posição.
Se o valor é encontrado logo nas primeiras verificações, o algoritmo encerra a execução imediatamente.

```

* **b) O que acontece quando o elemento procurado não existe?**

```
O algoritmo é forçado a percorrer todos os elementos da matriz do início ao fim sem interrupções,
resultando no número máximo possível de comparações.

```

* **c) Qual é o pior caso da busca sequencial?**

```
O pior caso ocorre quando o elemento procurado está localizado na última posição da matriz ou quando ele está ausente,
exigindo a varredura completa de toda a estrutura.

```

* **d) Como o aumento das dimensões da matriz influencia a quantidade de operações?**

```
O número de operações no pior caso cresce de forma diretamente proporcional ao número total de elementos da matriz.
Se as dimensões aumentam, o número máximo de comparações cresce na mesma proporção.

```

* **e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?**

```
A complexidade no pior caso é linear em relação ao número total de elementos,
correspondendo ao produto entre o número de linhas e o número de colunas.

```
