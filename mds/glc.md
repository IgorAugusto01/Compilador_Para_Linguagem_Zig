```
programa -> funcao  |
            decl |
            funcao programa |
            decl programa


funcao -> "pub" "fn" ID "("params")" tipo_retorno "{"decl_interna"}" |
        "pub" "fn" ID "()" tipo_retorno "{"decl_interna"}" |

          "fn" ID "("params")" tipo_retorno "{"decl_interna"}|
          "fn" ID "()" tipo_retorno "{"decl_interna"}"


          "pub" "fn" ID "("params")" tipo_retorno "{""}" |
        "pub" "fn" ID "()" tipo_retorno "{""}" |

          "fn" ID "("params")" tipo_retorno "{""}|
          "fn" ID "()" tipo_retorno "{""}"

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
              expr ";" |
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
              expr ";" |
             "var" ID ":" tipo_retorno "=" expr ";"  decl_interna|
              "const" ID = expr ";" decl_interna|
              "const" ID ":" tipo_retorno"=" expr ";" ecl_interna  |
              ID "=" expr ";" | decl_interna 
              ID "+=" expr ";" decl_interna|
              ID "+%" expr ";" decl_interna|
              ID "+%=" expr ";" decl_interna|
              ID "+|" expr ";" decl_interna|
              ID "+|=" expr ";" decl_interna|
              ID "-=" expr ";" decl_interna|
              ID "-%" expr ";" decl_interna|
              ID "-%=" expr ";" decl_interna|
              ID "-|" expr ";" decl_interna|
              ID "-|=" expr ";" decl_interna|
              expr ";"  decl_interna|
              BREAK ";" decl_interna
              RETURN expr ";" decl_interna
              WHILE "(expr")" "{"decl_interna"}" decl_interna|
              FOR "("INTEGER ".." INTEGER ")" "|" ID "|" {"decl_interna"}"decl_interna|
              IF "("expr ")"{"decl_interna"decl_interna}

expr -> 
       ID "-" expr |
       ID "/" expr |
       ID "*" expr |
       ID ">" expr |
       ID "<" expr |
       ID "%" expr |
       ID "==" expr  |
       ID "and" expr |
       ID "or"  expr |
       ID "==" expr |
       ID "and"expr |
       ID "or" expr |
        TRUE        |  
        FALSE       |    
       INTEGER
       ID
       ID "." EXPR
       BUILTINIDENTIFIER "(STRING)" |
       BUILTINIDENTIFIER "(STRING)" "." expr|
       ID "+" expr |
        call

call -> ID "("args")" |
        ID "("")"

args -> ID "," args |
        ID |
        STRING "," "." "{"args"}"
        STRING "," "." "{""}"

params -> ID : tipo_retorno |
          ID : tipo_retorno, params |
```
