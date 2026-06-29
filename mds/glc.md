```
programa -> funcao  |
            comandos |
            funcao programa |
            comandos programa


funcao -> "pub" "fn" ID "("params")" tipo_retorno "{"corpo"}" |
        "pub" "fn" ID "()" tipo_retorno "{"corpo"}" |

          "fn" ID "("params")" tipo_retorno "{"corpo"}|
          "fn" ID "()" tipo_retorno "{"corpo"}"

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

corpo -> comandos

comandos -> comando |
            comando comandos

comando -> "var" ID ":" tipo_retorno "=" expr ";" |
              "const" ID = expr ";"|
              "const" ID ":" tipo_retorno "=" expr ";" |
              "var" ID ":" tipo_retorno "=" "("expr")" ";" |
              "const" ID = "("expr") ";"|
              "const" ID ":" tipo_retorno "=" "("expr")" ";" |
              "_" "=" expr ";" |
              ID "=" expr ";" | 
              ID "+=" expr ";"|
              ID "+%" expr ";"|
              ID "+%=" expr ";"|
              ID "+|" expr ";"|
              ID "+|=" expr ";"|
              ID "-=" expr ";"|
              ID "-%" expr ";"|
              ID "-%=" expr ";"|
              ID "-|" expr ";"|
              ID "-|=" expr ";"|
              WHILE "(expr")" "{"comandos"}" |
              FOR "("expr ".." expr ")" |
              RETURN expr ";"

expr -> ID |
        ID "." expr |
        INTEGER |
        CHAR|
        STRING|
        BUILTINIDENTIFIER "(STRING)" |
        BUILTINIDENTIFIER "(STRING)" "." expr|
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
        ID "==" ID  |
        ID "and" ID |
        ID "or"  ID |
        INTEGER "==" ID  |
        INTEGER "and" ID |
        INTEGER "or"  ID |
        ID "=="  INTEGER |
        ID "and" INTEGER |
        ID "or"  INTEGER |
        INTEGER "=="  INTEGER |
        INTEGER "and" INTEGER |
        INTEGER "or"  INTEGER |
        TRUE        |  
        FALSE       |    
        call

call -> ID "("args")" |
        ID "("")"

args -> expr "," args |
        expr

params -> ID : tipo_retorno |
          ID : tipo_retorno, params |
```
