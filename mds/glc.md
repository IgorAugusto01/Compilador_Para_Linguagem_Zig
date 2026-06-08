# GLC da Linguagem de Programação Zig
---

Um programa Zig essecialmente precisa ter uma função main podendo ou não ser seguido ou precedido de funções adicionais e/ou declarações de nivel superior (variáveis ou constates fora do bloco main). A ordem que cada uma aparece não importa, contanto que tenha a função main, o programa irá ser executado normalmente.

---
```
programa -> fun_main  |
            funs_add programa |
            decls_sup programa
            
```

---


As funções precisam começar com a assinatura e o corpo da função. A assinatura pode ser a genérica que envolve as funções adicionais ou pode ser a assinatura da função main.

---

```
assinatura_gen -> "fn" ID "(" parametros ")" tipo_retorno |
                  "fn" ID "(" ")" tipo_retorno 
 
assinatura_main -> "fn" "main" "(" parametros ")" tipo_retorno |
                  "fn" ID "(" ")" tipo_retorno 
 

tipo_retorno -> void |
                i8 |
                u8 |
                i16 |
                u16 |
                i32 |
                u32 |
                i64 |
                u64 |
                i128 |
                u128

funs_add -> fun_add |
            fun_add funs_add |
            



```