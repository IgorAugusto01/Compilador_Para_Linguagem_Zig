import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

def p_error(p):
    if p is None:
        print("Erro sintático: fim inesperado do arquivo.")
        return

    print(
        f"Erro sintático na linha {p.lineno}, "
        f"token={p.type}, valor={p.value}"
    )



def p_programa_funcao(p):
    'programa : funcao'
    p[0] = sa.Programa_Funcao(p[1])

def p_programa_comandos(p):
    'programa : comandos'
    p[0] = sa.Programa_Comandos(p[1])

def p_programa_funcao_programa(p):
    'programa : funcao programa'
    p[0] = sa.Programa_Funcao_Programa(p[1], p[2])

def p_programa_comandos_programa(p):
    'programa : comandos programa'
    p[0] = sa.Programa_Comandos_Programa(p[1], p[2])
    
      
      
def p_funcao_pub_fn_params(p):
    '''
    funcao : PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE
    '''
    p[0] = sa.Funcao_Pub_Fn_Params(
        p[3],  # ID
        p[5],  # params
        p[7],  # tipo_retorno
        p[9]   # corpo
    )


def p_funcao_pub_fn(p):
    '''
    funcao : PUB FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE
    '''
    p[0] = sa.Funcao_Pub_Fn(
        p[3],  # ID
        p[6],  # tipo_retorno
        p[8]   # corpo
    )


def p_funcao_fn_params(p):
    '''
    funcao : FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE
    '''
    p[0] = sa.Funcao_Fn_Params(
        p[2],  # ID
        p[4],  # params
        p[6],  # tipo_retorno
        p[8]   # corpo
    )


def p_funcao_fn(p):
    '''
    funcao : FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE
    '''
    p[0] = sa.Funcao_Fn(
        p[2],  # ID
        p[5],  # tipo_retorno
        p[7]   # corpo
    )




def p_comandos_comando(p):
    'comandos : comando'
    p[0] = sa.Comandos_Comando(p[1])




def p_comandos_comando_comandos(p):
    'comandos : comando comandos'
    p[0] = sa.Comandos_Comando_Comandos(
        p[1],
        p[2]
    )




def p_tipo_retorno_void(p):
    'tipo_retorno : VOID'
    p[0] = sa.TipoRetorno_Void()

def p_tipo_retorno_i8(p):
    'tipo_retorno : I8'
    p[0] = sa.TipoRetorno_I8()

def p_tipo_retorno_u8(p):
    'tipo_retorno : U8'
    p[0] = sa.TipoRetorno_U8()

def p_tipo_retorno_i16(p):
    'tipo_retorno : I16'
    p[0] = sa.TipoRetorno_I16()

def p_tipo_retorno_u16(p):
    'tipo_retorno : U16'
    p[0] = sa.TipoRetorno_U16()

def p_tipo_retorno_i32(p):
    'tipo_retorno : I32'
    p[0] = sa.TipoRetorno_I32()

def p_tipo_retorno_u32(p):
    'tipo_retorno : U32'
    p[0] = sa.TipoRetorno_U32()

def p_tipo_retorno_i64(p):
    'tipo_retorno : I64'
    p[0] = sa.TipoRetorno_I64()

def p_tipo_retorno_u64(p):
    'tipo_retorno : U64'
    p[0] = sa.TipoRetorno_U64()

def p_tipo_retorno_i128(p):
    'tipo_retorno : I128'
    p[0] = sa.TipoRetorno_I128()

def p_tipo_retorno_u128(p):
    'tipo_retorno : U128'
    p[0] = sa.TipoRetorno_U128()



def p_corpo(p):
    'corpo : comandos'
    p[0] = sa.Corpo_Comandos(p[1])




def p_params_id_tipo_retorno(p):
    'params : ID COLON tipo_retorno'
    p[0] = sa.Params_ID_TipoRetorno(
        p[1],
        p[3]
    )


def p_params_id_tipo_retorno_params(p):
    'params : ID COLON tipo_retorno COMMA params'
    p[0] = sa.Params_ID_TipoRetorno_Params(
        p[1],
        p[3],
        p[5]
    )


def p_comando_var_id_tipo_expr(p):
    'comando : VAR ID COLON tipo_retorno EQUAL expr SEMICOLON'
    p[0] = sa.Comando_ID_TipoRetorno_Expr(p[2], p[4], p[6])


def p_comando_const_id_expr(p):
    'comando : CONST ID EQUAL expr SEMICOLON'
    p[0] = sa.Comando_ID_Expr(p[2], p[4])


def p_comando_const_id_tipo_expr(p):
    'comando : CONST ID COLON tipo_retorno EQUAL expr SEMICOLON'
    p[0] = sa.Comando_ID_TipoRetorno_Expr_2(p[2], p[4], p[6])


def p_comando_var_id_tipo_paren_expr(p):
    'comando : VAR ID COLON tipo_retorno EQUAL LPAREN expr RPAREN SEMICOLON'
    p[0] = sa.Comando_ID_TipoRetorno_Expr_3(p[2], p[4], p[7])


def p_comando_const_id_paren_expr(p):
    'comando : CONST ID EQUAL LPAREN expr RPAREN SEMICOLON'
    p[0] = sa.Comando_ID_Expr_2(p[2], p[5])


def p_comando_const_id_tipo_paren_expr(p):
    'comando : CONST ID COLON tipo_retorno EQUAL LPAREN expr RPAREN SEMICOLON'
    p[0] = sa.Comando_ID_TipoRetorno_Expr_4(p[2], p[4], p[7])


def p_comando_atribuicao(p):
    'comando : ID EQUAL expr SEMICOLON'

    if p[1] == "_":
        p[0] = sa.Comando_Expr(p[3])         
    else:
        p[0] = sa.Comando_ID_Expr_3(p[1], p[3])

def p_comando_add_eq(p):
    'comando : ID PLUSEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '+='")
    p[0] = sa.Comando_ID_Expr_4(p[1], p[3])


def p_comando_add_mod(p):
    'comando : ID PLUSPERCENT expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '+%'")
    p[0] = sa.Comando_ID_Expr_5(p[1], p[3])


def p_comando_add_mod_eq(p):
    'comando : ID PLUSPERCENTEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '+%='")
    p[0] = sa.Comando_ID_Expr_6(p[1], p[3])


def p_comando_add_sat(p):
    'comando : ID PLUSPIPE expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '+|'")
    p[0] = sa.Comando_ID_Expr_7(p[1], p[3])


def p_comando_add_sat_eq(p):
    'comando : ID PLUSPIPEEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '+|='")
    p[0] = sa.Comando_ID_Expr_8(p[1], p[3])


def p_comando_sub_eq(p):
    'comando : ID MINUSEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '-='")
    p[0] = sa.Comando_ID_Expr_9(p[1], p[3])


def p_comando_sub_mod(p):
    'comando : ID MINUSPERCENT expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '-%'")
    p[0] = sa.Comando_ID_Expr_10(p[1], p[3])


def p_comando_sub_mod_eq(p):
    'comando : ID MINUSPERCENTEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '-%='")
    p[0] = sa.Comando_ID_Expr_11(p[1], p[3])


def p_comando_sub_sat(p):
    'comando : ID MINUSPIPE expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '-|'")
    p[0] = sa.Comando_ID_Expr_12(p[1], p[3])


def p_comando_sub_sat_eq(p):
    'comando : ID MINUSPIPEEQUAL expr SEMICOLON'

    if p[1] == "_":
        raise SyntaxError("'_' não pode ser usado com '-|='")
    p[0] = sa.Comando_ID_Expr_12(p[1], p[3])
    

def p_comando_for(p):
    'comando : FOR LPAREN expr DOT2 expr RPAREN PIPE ID PIPE LBRACE comandos RBRACE'
    p[0] = sa.Comando_For(
        p[3],
        p[5],
        p[8],
        p[11]
    )
    
    
def p_comando_while(p):
    'comando : WHILE LPAREN expr RPAREN LBRACE comandos RBRACE'
    p[0] = sa.Comando_Expr_Comandos(
        p[3],
        p[6]
    )
    
    
def p_comando_return(p):
    'comando : RETURN expr SEMICOLON'
    p[0] = sa.Comando_Expr_13(p[2])
    
    
    
def p_expr_id(p):
    'expr : ID'
    p[0] = sa.Expr_ID(p[1])


def p_expr_id_expr(p):
    'expr : ID DOT expr'
    p[0] = sa.Expr_ID_Expr(p[1], p[3])


def p_expr_integer(p):
    'expr : INTEGER'
    p[0] = sa.Expr_INTEGER(p[1])


def p_expr_char(p):
    'expr : CHAR'
    p[0] = sa.Expr_CHAR(p[1])


def p_expr_string(p):
    'expr : STRING'
    p[0] = sa.Expr_STRING(p[1])


def p_expr_builtin_string(p):
    'expr : BUILTINIDENTIFIER LPAREN STRING RPAREN'
    p[0] = sa.Expr_BUILTINIDENTIFIER_STRING(p[1], p[3])


def p_expr_builtin_string_expr(p):
    'expr : BUILTINIDENTIFIER LPAREN STRING RPAREN DOT expr'
    p[0] = sa.Expr_BUILTINIDENTIFIER_STRING_Expr(p[1], p[3], p[6])


def p_expr_integer_add(p):
    'expr : INTEGER PLUS expr'
    p[0] = sa.Expr_INTEGER_Expr(p[1], p[3])




def p_expr_integer_sub(p):
    'expr : INTEGER MINUS expr'
    p[0] = sa.Expr_INTEGER_Expr_3(p[1], p[3])


def p_expr_integer_div(p):
    'expr : INTEGER SLASH expr'
    p[0] = sa.Expr_INTEGER_Expr_4(p[1], p[3])


def p_expr_integer_mul(p):
    'expr : INTEGER ASTERISK expr'
    p[0] = sa.Expr_INTEGER_Expr_5(p[1], p[3])


def p_expr_integer_gt(p):
    'expr : INTEGER RARROW expr'
    p[0] = sa.Expr_INTEGER_Expr_6(p[1], p[3])


def p_expr_integer_lt(p):
    'expr : INTEGER LARROW expr'
    p[0] = sa.Expr_INTEGER_Expr_6(p[1], p[3])


def p_expr_id_add(p):
    'expr : ID PLUS expr'
    p[0] = sa.Expr_ID_Expr_2(p[1], p[3])


def p_expr_id_sub(p):
    'expr : ID MINUS expr'
    p[0] = sa.Expr_ID_Expr_3(p[1], p[3])


def p_expr_id_div(p):
    'expr : ID SLASH expr'
    p[0] = sa.Expr_ID_Expr_4(p[1], p[3])


def p_expr_id_mul(p):
    'expr : ID ASTERISK expr'
    p[0] = sa.Expr_ID_Expr_5(p[1], p[3])


def p_expr_id_gt(p):
    'expr : ID RARROW expr'
    p[0] = sa.Expr_ID_Expr_6(p[1], p[3])


def p_expr_id_lt(p):
    'expr : ID LARROW expr'
    p[0] = sa.Expr_ID_Expr_7(p[1], p[3])


def p_expr_true(p):
    'expr : TRUE'
    p[0] = sa.Expr_True()


def p_expr_false(p):
    'expr : FALSE'
    p[0] = sa.Expr_False()


def p_expr_call(p):
    'expr : call'
    p[0] = sa.Expr_Call(p[1])
    

    
    
    
def p_call_id_id(p):
    'call : ID DOT ID LPAREN RPAREN'
    p[0] = sa.Call_ID_ID(
        p[1],
        p[3]
    )


def p_call_id_id_args(p):
    'call : ID DOT ID LPAREN args RPAREN'
    p[0] = sa.Call_ID_ID_Args(
        p[1],
        p[3],
        p[5]
    )


def p_call_id_id_id(p):
    'call : ID DOT ID DOT ID LPAREN RPAREN'
    p[0] = sa.Call_ID_ID_ID(
        p[1],
        p[3],
        p[5]
    )


def p_call_id_id_id_args(p):
    'call : ID DOT ID DOT ID LPAREN args RPAREN'
    p[0] = sa.Call_ID_ID_ID_Args(
        p[1],
        p[3],
        p[5],
        p[7]
    )


def p_args_expr_args(p):
    'args : expr COMMA args'
    p[0] = sa.Args_Expr_Args(p[1], p[3])


def p_args_expr(p):
    'args : expr'
    p[0] = sa.Args_Expr(p[1])
    
    
    
def main():
    f = open("ex/exemplo.zig", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()