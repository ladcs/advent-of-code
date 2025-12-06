# Advent of Code

O Advent of Code é uma série de desafios diários que acontecem todo mês de dezembro, sempre divididos em duas partes.
Decidi que em 2025 iria fazer e registrar algumas soluções que achei interessantes — e também alguns problemas legais que precisei resolver no caminho.

Abaixo compartilho meu raciocínio dia a dia, incluindo insights, problemas encontrados e soluções robustas que desenvolvi.

📅 Dia 1 — Roleta circular (wrap-around)

O desafio envolve uma roleta de 0 a 99. Cada comando vem no formato:

LX → mover X para a esquerda (subtrair)

RX → mover X para a direita (somar)

A roleta é circular:

de 99 e aplicar R2 → vai para 1

de 0 e aplicar L2 → vai para 98

O número inicial é 50, e cada resultado vira o offset da próxima operação.

Parte 1

Contar quantas vezes o valor resultante é 0.

Solução

Usei a lógica de wrap-around com módulo:

novo_valor = (valor_atual + deslocamento) % 100


Exemplos:

R50 → (50 + 50) % 100 = 0

L10 → (50 - 10) % 100 = 40

Simples e eficiente.

Parte 2

Agora preciso também contar quantas vezes a roleta passa pelo 0, mesmo que não pare nele.

Exemplos:

Começa em 50, R52 → passa 1 vez por 0

Começa em 50, R150 → passa 1 vez e termina em 0 → conta 2

Começa em 50, R1000 → passa 50 vezes

Primeira tentativa

Usei a lógica:

se for R e o valor final é menor que o inicial → passou pelo zero

se for L e o final é maior → passou pelo zero

somar também abs(X) // 100 para contar voltas completas

Problemas encontrados

Se começar em 0 e aplicar operação, contava indevidamente uma passagem extra

Quando X > 100 e terminava em 0, eu contava 2 vezes o zero (duplicado)

Solução final

Só contar passagem se a operação não começar ou terminar em 0.
Isso garantiu que o zero fosse contabilizado corretamente apenas quando realmente atravessado.

📅 Dia 2 — Intervalos numéricos e padrões repetidos

Entrada no formato "x-y".
Objetivo: encontrar números dentro do intervalo que seguem padrões específicos.

Parte 1 — Números que repetem sua primeira metade

Exemplos válidos:

11, 22 em 11–22

1010 em 998–1012 (repete “10”)

Lógica utilizada

Pegar quantidade de dígitos do início e do fim do intervalo.

Para números com dígitos pares:

dividir em 2

duplicar a primeira metade

ex.: 123456 → 123|123

Se o número gerado estiver abaixo do intervalo:

incrementar a metade e tentar novamente

Se o início do intervalo tiver dígitos ímpares e o final tiver pares:

começar pela menor metade possível que gere um número válido de mesmo tamanho do limite superior.
Ex.: intervalo 998–1024 → começo a testar a partir de 1000.

Funcionou perfeitamente.

Parte 2 — Números formados por repetição integral de um bloco

Exemplos válidos:

11, 111, 1111 → repete “1”

1010, 101010 → repete “10”

123123123 → repete “123”

Confesso fiz força bruta: testar cada número do intervalo e verificar repetições.
Funcionou, mas não gostei da solução.

Solução pare testar futuramente.

Acredito que poderia gerar diretamente os números que são repetições, sem testar um por um.

Exemplo:

intervalo: 110–10000

1️⃣ Repetições de 1 dígito

Gerar:

111, 1111, 11111
222, 2222, 22222
...
999, 9999, 99999


Os últimos são descartado pois ultrapassam 10000.

2️⃣ Repetições de 2 dígitos

Com bloco de 2 dígitos posso gerar números de:

4 dígitos → ok

6 dígitos → já extrapola o limite de 5 dígitos → descarta

Exemplo:

11 → 1111
12 → 1212
...
99 → 9999

3️⃣ Repetições de 3 dígitos

Bloco de 3 dígitos gera:

6 dígitos → ultrapassa limite de 5 → não serve
Ignorado.

4️⃣ Agregação

Todos os números gerados vão para um set() para remover duplicatas.
Depois somo apenas os que estão no intervalo.

📅 Dia 3 — Construindo o maior número possível mantendo ordem

O input é uma sequência, como:

123455811119112


Na parte 1, o objetivo é construir o maior número de 2 dígitos, mantendo a ordem dos originais.

Estratégia:

Removo o último número

Procuro o maior entre os 14 restantes para o primeiro dígito

Para o segundo dígito, ignoro tudo com índice ≤ do primeiro escolhido

Escolho o maior do restante

Simples e funcional.

Parte 2 — 12 dígitos

Mesma lógica — porém agora com janelas deslizantes.

Percebi que para gerar 12 dígitos a partir de 15 números:

o primeiro dígito só pode ser escolhido entre os 4 primeiros

dependendo da posição escolhida, a janela de escolhas seguintes encolhe

Exemplo:

Se na primeira escolha o número escolhido for um dos primeiros no array, a próxima escolha terá um liberdade maior. No caso atual a primeira escolha te liberdade de 4, se o primeiro número foi a primeira escolha a segunda tera a liberdade de 4 números, ja se a primeira escolha for o segundo número a próxima escolha tera liberdade entre 3 e assim por diante.

Foi um caso interessante de observar impacto de "janela de deslizamento" na decisão.

O bom que o pensamento dessa parte pode ser usando para n digitos, inclusive para 2 digitos.

📅 Dia 4 — Matriz e adjacências

Input: matriz com @ e .
Sempre que um @ tiver menos de 4 adjacentes (incluindo diagonais), algo deve ser feito.

Parte 1 — Contar @ com exatamente 3 adjacentes

Identifiquei posições fronteira (linhas e colunas extremas assim como @ adjacente aos .).

A partir dessas posições, procuro @.

Para cada @, conto adjacentes — se tiver 3, acumulo.

Parte 2 — Quantos @ podem ser removidos

Processo iterativo:

Usar a mesma detecção da parte 1

Substituir @ por . quando tem ≤ 3 adjacentes

Repetir até não existir mais @ removível

📅 Dia 5 — Intervalos e IDs válidos

Input:

lista de intervalos (x-y)

lista de IDs

Parte 1 — Quantos IDs estão em algum intervalo

Faça merge de intervalos que se sobrepõem

ex.: 16–20 e 12–18 → viram 12–20

Para cada ID da lista, verifico se está dentro de algum intervalo mesclado

Conto

Parte 2 — Quantos valores existem dentro dos intervalos

Para cada intervalo mesclado:

quantidade = (fim + 1) - início

Depois somar tudo.

📅 Dia 6 — Cephalopod Math (colunas invertidas)

Input:

matriz de números (com espaços representando ausência de dígitos)

última linha contendo símbolos * ou +

leitura especial: da direita para a esquerda, de cima para baixo

Parte 1 — Soma ou multiplicação por coluna

Ler a matriz normalmente

Remover espaços de cada célula

Para cada coluna:

Se o símbolo na última linha for +, somar os números da coluna

Se for *, multiplicar

Somar todos os resultados

Parte 2 — Interpretar números verticalmente, da direita para a esquerda

Regra do input:
Cada coluna deve ser lida de cima para baixo, mas as colunas precisam ser processadas da direita para a esquerda.
Espaços contam como “sem dígito”.

Minha dificuldade

Tentei primeiro reconstruir a matriz já no formato final conforme a regra

Isso me levou a criar 3 loops aninhados

Funcionava no input de exemplo, mas quebrava no input real

Além disso, a solução estava ficando lenta e desnecessariamente complexa

Como resolvi

Percebi que o problema estava em tentar montar a matriz final depois de ler o arquivo

Então troquei a abordagem:

✔️ Ler o input por colunas em vez de por linhas
✔️ Criar uma matriz transposta diretamente na leitura
✔️ Com isso, obtive algo como uma lista de tuplas contendo cada coluna completa

Exemplo de estrutura intermediária:

('1',' ',' ','*')
('2','4',' ',' ')
('3','5','6',' ')
...


Depois foi só:

Fazer .join() na tupla

Remover espaços

Identificar * ou + no primeiro caractere válido

Tratar o restante como número

Aplicar a operação correspondente