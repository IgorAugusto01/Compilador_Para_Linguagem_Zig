```
programa -> funcao  |
            decl |
            funcao programa |
            decl programa


funcao -> "pub" "fn" ID "("params")" tipo_retorno "{"decl_interna"}" |
        "pub" "fn" ID "()" tipo_retorno "{"decl_interna"}" |

          "fn" ID "("params")" tipo_retorno "{"decl_interna"}|
          "fn" ID "()" tipo_retorno "{"decl_interna"}"

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


decl -> "var" ID ":" tipo_retorno "=" expr ";" |
              "const" ID = expr ";"|
              "const" ID ":" tipo_retorno "=" expr ";" |
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

decl_interna -> "var" ID ":" tipo_retorno "=" expr ";" |
              "const" ID = expr ";"|
              "const" ID ":" tipo_retorno "=" expr ";" |
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
              BREAK ";"
              RETURN expr ";"
              WHILE "(expr")" "{"comandos"}" |
              FOR "("expr ".." expr ")" "|" expr "|" {"comandos"}"|
              IF "("expr ")"{"comandos"}

expr -> ID |
        ID "." expr |
        INTEGER
        CHAR|
        STRING|
        BUILTINIDENTIFIER "(expr)" |
       BUILTINIDENTIFIER "(expr)" "." expr|
       expr "+" expr |
       expr "-" expr |
       expr "/" expr |
       expr "*" expr |
       expr ">" expr |
       expr "<" expr |
       expr "%" expr |
       expr "==" expr  |
       expr "and" expr |
       expr "or"  expr |
       expr "==" expr |
       expr "and"expr |
       expr "or" expr |
        TRUE        |  
        FALSE       |    
        call

call -> expr "("args")" |
        expr "("")"
        expr "("args "," "." "{"args"}" ")" |
        expr "("args "," "." "{"args"}" ")" 

args -> expr "," args |
        expr

params -> expr : tipo_retorno |
          expr : tipo_retorno, params |
```
