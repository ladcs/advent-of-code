# 🎄 Advent of Code 2025 — Minhas Soluções, Insights e Dificuldades

O Advent of Code é uma série de desafios diários que acontecem todo mês de dezembro, sempre divididos em duas partes.  
Decidi que em 2025 iria fazer e registrar algumas soluções que achei interessantes — e também alguns problemas legais que precisei resolver no caminho.

Abaixo compartilho meu raciocínio dia a dia, incluindo insights, problemas encontrados e soluções robustas que desenvolvi.

---

## 📅 Dia 1 — Roleta circular (wrap-around)

O desafio envolve uma roleta de 0 a 99. Cada comando vem no formato:

- `LX` → mover X para a esquerda (subtrair)  
- `RX` → mover X para a direita (somar)

A roleta é circular:

- de 99 e aplicar `R2` → vai para 1  
- de 0 e aplicar `L2` → vai para 98  

O número inicial é **50**, e cada resultado vira o offset da próxima operação.

### **Parte 1 — Quantas vezes o valor resultante é 0**

Usei a lógica de wrap-around com módulo:

novo_valor = (valor_atual + deslocamento) % 100


Exemplos:

- `R50` → (50 + 50) % 100 = **0**  
- `L10` → (50 - 10) % 100 = **40**  

Simples e eficiente.

---

### **Parte 2 — Quantas vezes a roleta passa pelo zero**

Regras:

- Começa em 50, `R52` → passa **1 vez** por 0  
- Começa em 50, `R150` → passa 1 vez e termina em 0 → **conta 2**  
- Começa em 50, `R1000` → passa **50 vezes**

#### Primeira tentativa

- se for **R** e o valor final é menor que o inicial → passou pelo zero  
- se for **L** e o final é maior → passou pelo zero  
- somar também `abs(X) // 100` para voltas completas  

#### Problemas

- começando em 0, eu contava uma passagem extra  
- quando terminava em 0, contava 2 vezes indevidamente  

#### Solução final

Só conto passagem se **a operação não começar ou terminar em 0**.  
Isso eliminou duplicações e tornou o cálculo correto.

---

## 📅 Dia 2 — Intervalos numéricos e padrões repetidos

Entrada no formato `x-y`.  
Objetivo: encontrar números dentro do intervalo que seguem padrões específicos.

---

### **Parte 1 — Números que repetem sua primeira metade**

Exemplos válidos:

- `11`, `22`
- `1010` (repete “10”)

#### Lógica utilizada

- pegar quantidade de dígitos do início e do fim do intervalo  
- para números com dígitos pares:
  - dividir em 2
  - duplicar a primeira metade  
- se o número gerado for menor que o início do intervalo:  
  - incrementar a metade e gerar de novo  
- se o início tem dígitos ímpares e o final pares:
  - gerar a partir do menor número possível com dígitos pares compatíveis  

Funcionou muito bem.

---

### **Parte 2 — Números formados por repetição integral de um bloco**

Exemplos válidos:

- `11`, `111`, `1111`  
- `1010`, `101010`  
- `123123123`

#### Minha solução inicial

Fiz **força bruta**: testar cada número e verificar se é repetição.

Funciona, mas não gostei.

#### Ideia futura (mais elegante)

Gerar apenas números que são repetições, sem testar todos do intervalo.

Exemplo para `110–10000`:

1. **Repetições de 1 dígito**
   - 111, 1111, 11111  
   - 222, 2222, 22222  
   - …  
   - 999, 9999, 99999  
   (descartar maiores que o limite)

2. **Repetições de 2 dígitos**
   - Ex.: 12 → 1212  
   - Só números de 4 dígitos servem  
   - 6 dígitos já extrapola

3. **Repetições de 3 dígitos**
   - Gerariam 6 dígitos → excede 5 → ignorado

Gerar tudo, colocar num `set()`, e filtrar apenas os que caem no intervalo.

---

## 📅 Dia 3 — Construindo o maior número possível mantendo ordem

Input:

123455811119112


### **Parte 1 — Maior número de 2 dígitos**

Estratégia:

1. Remover o último número  
2. Procurar o maior dos 14 restantes como primeiro dígito  
3. Para o segundo dígito:
   - ignorar índices ≤ ao escolhido  
   - escolher o maior do restante  

### **Parte 2 — Maior número de 12 dígitos**

Aqui a janela de escolhas desliza:

- Para gerar 12 dígitos a partir de 15:
  - o primeiro dígito só pode ser escolhido entre os **4 primeiros**
- Quanto mais à direita a escolha, menor a janela seguinte

Esse raciocínio funciona para qualquer N.

---

## 📅 Dia 4 — Matriz e adjacências

Input: matriz com `@` e `.`  
Adjacências incluem diagonais.

---

### **Parte 1 — Contar @ com exatamente 3 adjacentes**

- Identificar regiões fronteira  
- Verificar cada `@`  
- Contar adjacentes  
- Somar apenas os que têm **3 adjacentes**

---

### **Parte 2 — Quantos @ podem ser removidos**

Processo iterativo:

1. Detectar `@` com ≤ 3 adjacentes  
2. Substituir por `.`  
3. Repetir até estabilizar  

---

## 📅 Dia 5 — Intervalos e IDs válidos

Input:

- lista de intervalos (x-y)  
- lista de IDs  

---

### **Parte 1 — IDs dentro de algum intervalo**

- Mesclar intervalos sobrepostos  
  - ex.: `16–20` e `12–18` → `12–20`  
- Verificar para cada ID  
- Contar

---

### **Parte 2 — Quantos valores existem dentro dos intervalos**

Para cada intervalo mesclado:

quantidade = (fim + 1) - início


Depois somar tudo — simples e direto.

---

## 📅 Dia 6 — Cephalopod Math (colunas invertidas)

Input:

- Matriz de dígitos (com espaços significando ausência)
- Última linha: símbolos `*` ou `+`
- Leitura especial:  
  **colunas de cima para baixo**, mas processando **da direita para a esquerda**

---

### **Parte 1 — Soma ou multiplicação por coluna**

Passos:

1. Ler matriz normalmente  
2. Remover espaços  
3. Para cada coluna:  
   - `+` → soma  
   - `*` → multiplicação  
4. Somar os resultados

---

### **Parte 2 — Interpretar números verticalmente e ao contrário**

A regra:

- cada coluna é um número formado verticalmente  
- o processamento ocorre da direita para a esquerda  
- espaços são “não dígitos”

---

### **Minha dificuldade**

Minha primeira abordagem:

❌ tentar gerar toda a matriz final depois de ler o arquivo  
❌ loops aninhados  
❌ funcionava no exemplo, **quebrava no input real**  
❌ solução ficando lenta e complexa  

---

### **Solução final — Ler por colunas**

Troquei a estratégia:

✔️ ler o input **por colunas**, não por linhas  
✔️ criar a matriz já transposta  
✔️ gerar tuplas representando as colunas completas

Exemplo:

('1',' ',' ','*')
('2','4',' ',' ')
('3','5','6',' ')
...


Depois foi só:

- usar `.join()` na tupla  
- remover espaços  
- identificar `*` ou `+`  
- tratar o resto como número  
- aplicar a operação correta  

Simples, rápido e elegante.

---

