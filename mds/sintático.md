# Documentação Sintática da Linguagem de Programação Zig
---

Um programa Zig pode ser composto por uma função e/ou comandos.

---
```
programa -> funcao  |
            comandos |
            funcao programa |
            comandos programa
```

As funções em Zig por padrão são privadas, elas podem ou não vir com o prefixo "pub", mas necessitam estar com "fn", ID, parênteses contendo ou não parâmetros, dois pontos, o tipo de retorno, além das chaves contendo o corpo da função.

```
funcao -> "pub" "fn" ID "("params")" tipo_retorno "{"corpo"}" |
        "pub" "fn" ID "()" tipo_retorno "{"corpo"}" |

          "fn" ID "("params")" tipo_retorno "{"corpo"}|
          "fn" ID "()" tipo_retorno "{"corpo"}"
```

Os tipos de retorno são:


```
 tipo_retorno -> "void" |
                  "i8" |
                  "u8" |
                 "i16" |
                 "u16" |
                 "i32" |
                 "u32" |
                 "i64" |
                 "u64" |
                "i128" |
                "u128
```

Os parâmetros são escritos assim: 

```
params -> ID : tipo_retorno |
          ID : tipo_retorno params |    
```

Um corpo pode conter comandos.

```
corpo ->  comandos|

comandos -> comando |
            comando comandos     
```
 
Um comando pode ser servido da palavra const, que pode ser especificado o tipo de retorno ou não, e a palavra var, que necessariamente precisa especificar o tipo de retorno. Todas essas palavras podem vir precedidas da palavra pub, além do while, for e return.

```
comando -> "var" ID ":" tipo_retorno "=" expr ";" |
              "const" ID = expr ";"|
              "const" ID ":" tipo_retorno "=" expr ";" |
              "var" ID ":" tipo_retorno "=" "("expr")" ";" |
              "const" ID = "("expr") ";"|
              "const" ID ":" tipo_retorno "=" "("expr")" ";" |
              "_" "=" expr ";" |
              WHILE "(expr")" "{"comandos"}" |
              FOR "("expr ".." expr ")" |
              RETURN expr ";"
```

As expressões são todas as possibilidades de retorno. Estão escritas abaixo.
```
expr -> ID |
        ID "." expr |
        INTEGER |
        CHAR|
        STRING|
        BUILTINIDENTIFIER "(STRING)" |
        BUILTINIDENTIFIER "(STRING)" "." ID "." expr|
        INTEGER "+" expr |
        INTEGER "+" expr |
        INTEGER "-" expr |
        INTEGER "/" expr |
        INTEGER "*" expr |
        INTEGER ">" expr |
        INTEGER "<" expr |
        ID "+" expr |
        ID "-" expr |
        ID "/" expr |
        ID "*" expr |
        ID ">" expr |
        ID "<" expr |
        TRUE        |  
        FALSE       |    
        call
   ``` 


Chamadas de função podem ser expressas com ou sem argumentos: 

 ```       
call -> ID "("args")" |
        ID "("")"

args -> expr "," args |
        expr              
```       


        
