# Meteor Challenge

## Tarefas

1. Count the number of Stars
2. Count the number of Meteors
3. If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water
4. (optional) Find the phrase that is hidden in the dots in the sky. 
   - HINT 1: 175 Characters
   - HINT 2: Most of the last tasks’ code can be reused for this one

## Explicação do Código

1. **Contagem de Estrelas e Meteoros:**
   - Abri a imagem e obtive os dados dos pixels.
   - Iterei sobre cada pixel e verifiquei sua cor.
   - Contei as estrelas e meteoros com base em suas cores e atualizei a matriz binária (`phrase_bin`) para a frase oculta.

2. **Contagem de Meteoros Caindo na Água:**
   - Ao encontrar pixels com a cor da água, adicionei o índice da coluna ao conjunto `water_level`.
   - Para cada meteoro, verifiquei se ele estava na mesma coluna que a água e incrementei a contagem de `meteors_in_water` se estivesse.

3. **Frase Oculta:**
   - A princípio, pensei que a frase poderia ser codificada em código binário. Primeiramente, considerei o código Morse, onde meteoros seriam representados por traços (–) e estrelas por pontos (.), ou vice-versa, mas os resultados não faziam sentido.
   - Em seguida, tentei a tabela ASCII, assumindo que estrelas poderiam ser 0 e meteoros 1, mas isso não resultou em 175 caracteres.
   - Então, percebi que cada linha tinha 704 pixels. Se fossem duas linhas, isso daria 1408 bits, e dividindo por 8 (número de bits em um caractere ASCII) resultaria em 176 caracteres, o que fez mais sentido.
   - Após algumas tentativas e erros, identifiquei que uma linha poderia ser para estrelas e outra para meteoros, com elementos valendo 1 e os espaços 0, resultando na frase oculta.

## Feedback sobre o Desafio

As três primeiras tarefas foram triviais e relativamente fáceis de implementar. No entanto, a última tarefa, que envolvia desvendar a frase oculta, exigiu bastante tempo e esforço. Passei por várias tentativas e abordagens diferentes, desde considerar o código Morse até ajustar a interpretação binária para a tabela ASCII, antes de finalmente descobrir a frase secreta. Foi um desafio interessante e gratificante de resolver.