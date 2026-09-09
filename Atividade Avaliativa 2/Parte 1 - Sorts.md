Parte 1 – Sorts

Bubble Sort:

Como funciona: O algoritmo percorre o array várias vezes, comparando pares de elementos adjacentes. Se dois elementos estiverem na ordem incorreta, eles são trocados. A cada passagem completa, o maior elemento restante "borbulha" para a sua posição correta no final do vetor.

Lógica de ordenação: Utiliza dois loops aninhados. O loop externo controla o número de passagens, e o interno realiza as comparações e trocas adjacentes.

- Complexidade no melhor caso: O(n) (quando o array já está ordenado, utilizando uma flag de otimização).
- Complexidade no caso médio: O(n^2 ).
- Complexidade no pior caso: O(n^2 ) (quando o array está em ordem inversa).
- Vantagens: Simplicidade extrema de implementação e fácil compreensão conceitual; algoritmo estável.
- Limitações: Altamente ineficiente para grandes volumes de dados devido ao crescimento quadrático das operações.
- Situações em que seu uso é adequado: Pequenos conjuntos de dados ou coleções que já se encontram quase totalmente ordenadas.
- Situações em que seu uso não é recomendado: Grandes bases de dados ou aplicações em tempo real que exigem alta performance.

