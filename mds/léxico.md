# ✨ Linguagem Zig (Subset) - Elementos Léxicos

A linguagem implementada neste projeto é baseada na sintaxe da linguagem Zig e possui os seguintes elementos léxicos reconhecidos pelo analisador.

## 1. Palavras Reservadas

A linguagem possui as seguintes palavras reservadas:

```text
and        anytype     break       const
continue   else        enum        false
fn         for         if          or
orelse     pub         return      struct
switch     true        union       undefined
while      var         void

i8   u8
i16  u16
i32  u32
i64  u64
i128 u128
```

Essas palavras possuem significado especial na linguagem e não podem ser utilizadas como identificadores comuns.

---

## 2. Operadores

A linguagem reconhece os seguintes operadores.

### Operadores Aritméticos

| Operador | Descrição |
|-----------|------------|
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `%` | Resto da divisão |
| `^` | XOR bit a bit |

### Operadores de Atribuição

| Operador |
|-----------|
| `=` |
| `+=` |
| `-=` |
| `*=` |
| `/=` |
| `%=` |
| `^=` |
| `&=` |
| `|=` |
| `<<=` |
| `>>=` |
| `+%=` |
| `-%=` |
| `*%=` |
| `+|=` |
| `-|=` |
| `<<|=` |

### Operadores Relacionais

| Operador | Descrição |
|-----------|------------|
| `==` | Igual |
| `!=` | Diferente |
| `<` | Menor |
| `<=` | Menor ou igual |
| `>` | Maior |
| `>=` | Maior ou igual |

### Operadores Lógicos

| Operador |
|-----------|
| `and` |
| `or` |
| `!` |

### Operadores Bit a Bit

| Operador |
|-----------|
| `&` |
| `|` |
| `~` |
| `<<` |
| `>>` |

### Outros Operadores

| Operador |
|-----------|
| `->` |
| `=>` |
| `?` |
| `.` |
| `..` |
| `...` |
| `.*` |
| `.?` |

---

## 3. Delimitadores

A linguagem utiliza os seguintes delimitadores:

| Delimitador | Uso |
|------------|-----|
| `;` | Finalização de comandos |
| `,` | Separação de parâmetros |
| `:` | Separação de tipos e rótulos |
| `(` `)` | Agrupamento de expressões |
| `{` `}` | Blocos de comandos |
| `[` `]` | Vetores e indexação |

---

## 4. Identificadores

Um identificador válido deve iniciar com uma letra (`a-z`, `A-Z`) ou com o caractere `_`.

Após o primeiro caractere, podem aparecer:

- Letras (`a-z`, `A-Z`)
- Dígitos (`0-9`)
- Sublinhado (`_`)

Expressão regular utilizada:

```regex
[a-zA-Z_][a-zA-Z0-9_]*
```

### Exemplos Válidos

```zig
nome
_variavel
contador123
soma_total
```

### Exemplos Inválidos

```zig
123nome
@variavel
$valor
```

---

## 5. Identificadores Built-in

A linguagem reconhece identificadores especiais iniciados pelo símbolo `@`.

Expressão regular utilizada:

```regex
@[a-zA-Z_][a-zA-Z0-9_]*
```

### Exemplos

```zig
@import
@sizeOf
@typeInfo
```

---

## 6. Literais Numéricos (INTEIROS)

A linguagem suporta números inteiros sem sinal.

São aceitos os seguintes formatos.

### Decimal

```zig
0
10
12345
```

### Binário

Prefixo `0b`.

```zig
0b1010
0b11110000
```

### Octal

Prefixo `0o`.

```zig
0o755
0o123
```

### Hexadecimal

Prefixo `0x`.

```zig
0xFF
0x1A2B
```



Também é permitido o uso do caractere `_` como separador visual.

```zig
1_000_000
0b1111_0000
0xFF_FF
```

---

## 7. Literais de String

Strings são delimitadas por aspas duplas (`"`).

Expressão regular utilizada:

```regex
"([^"\\]|\\.)*"
```

### Exemplos

```zig
"Olá Mundo"
"abc"
"linha\n"
```

---

## 8. Literais de Caractere

Caracteres são delimitados por aspas simples (`'`).

Expressão regular utilizada:

```regex
'.'
```

### Exemplos

```zig
'a'
'b'
'1'
```

---

## 9. Comentários

A linguagem suporta comentários de linha iniciados por `//`.

Tudo que aparece após `//` até o final da linha é considerado comentário.

### Exemplo

```zig
// Este é um comentário
var x = 10;
```

---

## 10. Espaços em Branco

Os seguintes caracteres são ignorados pelo analisador léxico:

- Espaço (` `)
- Tabulação (`\t`)

As quebras de linha também são ignoradas para fins de geração de tokens, porém são utilizadas para atualizar a variável `lineno`, que indica a linha atual do código-fonte.

---

## 11. Erros Léxicos

Qualquer caractere que não pertença a nenhuma das categorias descritas anteriormente é considerado um erro léxico.

Quando um erro é encontrado, o analisador exibe a seguinte mensagem:

```text
Caractere inválido: <caractere>
```

e continua a análise a partir do próximo caractere.

### Exemplo

```zig
var x = 10 $ 20;
```

Saída:

```text
Caractere inválido: $
```

---

## 12. Observações

O analisador léxico foi implementado utilizando a biblioteca **PLY (Python Lex-Yacc)**. Durante a análise, os tokens identificados são classificados de acordo com as regras descritas neste documento e encaminhados para as etapas posteriores do compilador.