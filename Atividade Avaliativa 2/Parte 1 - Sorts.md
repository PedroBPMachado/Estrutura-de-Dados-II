###### PARTE 1 – PESQUISA: SORTS

#### Bubble Sort
* **Como funciona:** O algoritmo percorre o array várias vezes, comparando pares de elementos adjacentes. Se dois elementos estiverem na ordem incorreta, eles são trocados. A cada passagem completa, o maior elemento restante "borbulha" para a sua posição correta no final do vetor.
* **Lógica de ordenação:** Utiliza dois loops aninhados. O loop externo controla o número de passagens, e o interno realiza as comparações e trocas adjacentes.
* **Complexidade no melhor caso:** $O(n)$ (quando o array já está ordenado, utilizando uma flag de otimização).
* **Complexidade no caso médio:** $O(n^2)$.
* **Complexidade no pior caso:** $O(n^2)$ (quando o array está em ordem inversa).
* **Vantagens:** Simplicidade extrema de implementação e fácil compreensão conceitual; algoritmo estável.
* **Limitações:** Altamente ineficiente para grandes volumes de dados devido ao crescimento quadrático das operações.
* **Situações em que seu uso é adequado:** Pequenos conjuntos de dados ou coleções que já se encontram quase totalmente ordenadas.
* **Situações em que seu uso não é recomendado:** Grandes bases de dados ou aplicações em tempo real que exigem alta performance.

#### Quick Sort
* **Como funciona:** Baseia-se na estratégia de "Dividir para Conquistar". Escolhe-se um elemento como pivô e o array é particionado de modo que todos os elementos menores que o pivô fiquem à sua esquerda e os maiores à sua direita. O processo é aplicado recursivamente às partições.
* **Lógica de ordenação:** Particionamento e recursão. O array é dividido em subproblemas menores que são resolvidos independentemente.
* **Complexidade no melhor caso:** $O(n \log n)$ (quando o pivô divide o array exatamente ao meio em todas as etapas).
* **Complexidade no caso médio:** $O(n \log n)$.
* **Complexidade no pior caso:** $O(n^2)$ (quando o pivô escolhido é sempre o menor ou o maior elemento, como em arrays já ordenados com escolha ingênua de pivô).
* **Vantagens:** Altamente eficiente na prática para grandes volumes de dados; opera *in-place* (consome pouca memória auxiliar).
* **Limitações:** Instável por padrão; dependência crítica da escolha do pivô para evitar o pior caso.
* **Situações em que seu uso é adequado:** Ordenação geral de grandes volumes de dados onde o desempenho médio é prioridade.
* **Situações em que seu uso não é recomendado:** Dados com muitos elementos repetidos (se não otimizado) ou quando a estabilidade da ordenação original é um requisito obrigatório.

#### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **Princípio de funcionamento** | Comparação e troca de elementos adjacentes iterativamente. | Divisão e conquista com escolha de pivô e particionamento. |
| **Melhor caso** | $O(n)$ | $O(n \log n)$ |
| **Caso médio** | $O(n^2)$ | $O(n \log n)$ |
| **Pior caso** | $O(n^2)$ | $O(n^2)$ |
| **Uso de memória** | $O(1)$ (In-place) | $O(\log n)$ (Devido à pilha de recursão) |
| **Vantagem principal** | Simplicidade de código e estabilidade. | Velocidade superior em larga escala. |
| **Limitação principal** | Desempenho quadrático para grandes entradas. | Pior caso quadrático se o pivô for mal escolhido; instável. |
| **Aplicação recomendada** | Vetores muito pequenos ou quase ordenados. | Grandes conjuntos de dados genéricos. |

---
