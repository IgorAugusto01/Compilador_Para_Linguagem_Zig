import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

########################## REGRAS DE PRODUÇÃO PARA O PARSER #########################




def p_error(p):
    if p:
        print(f"Erro sintático em '{p.value}' (linha {p.lineno})")
    else:
        print("Erro sintático: fim inesperado do arquivo.")




###### Variável Programa #######

def p_programa_funcao(p):
    '''programa : funcao'''
    p[0] = sa.Programa_Funcao(p[1])

def p_programa_decl(p):
        '''programa : decl'''
        p[0] = sa.Programa_Decl(p[1])

def p_programa_funcao_programa(p):
        '''programa : funcao programa'''
        p[0] = sa.Programa_Funcao_Programa(p[1],p[2])

def p_programa_decl_programa(p):
        '''programa : decl programa'''
        p[0] = sa.Programa_Decl_Programa(p[1],p[2])
    
##### Variavel Funcao ######


def p_funcao_pub_fn_params_tipo_retorno_decl_interna(p):
    '''funcao : PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE decl_interna RBRACE'''
    p[0] = sa.Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(p[1], p[5], p[7], p[9])


def p_funcao_pub_fn_tipo_retorno_decl_interna(p):
    '''funcao : PUB FN ID LPAREN RPAREN tipo_retorno LBRACE decl_interna RBRACE'''
    p[0] = sa.Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna(p[1], p[6], p[8])


def p_funcao_fn_params_tipo_retorno_decl_interna(p):
    '''funcao : FN ID LPAREN params RPAREN tipo_retorno LBRACE decl_interna RBRACE'''
    p[0] = sa.Funcao_Fn_Params_Tipo_Retorno_Decl_Interna(p[4], p[6], p[8])


def p_funcao_fn_tipo_retorno_decl_interna(p):
    '''funcao : FN ID LPAREN RPAREN tipo_retorno LBRACE decl_interna RBRACE'''
    p[0] = sa.Funcao_Fn_Tipo_Retorno_Decl_Interna(p[5], p[7])


def p_funcao_pub_fn_params_tipo_retorno(p):
    '''funcao : PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE RBRACE'''
    p[0] = sa.Funcao_Pub_Fn_Params_Tipo_Retorno(p[1], p[5], p[7])




def p_funcao_fn_params_tipo_retorno(p):
    '''funcao : FN ID LPAREN params RPAREN tipo_retorno LBRACE RBRACE'''
    p[0] = sa.Funcao_Fn_Params_Tipo_Retorno(p[4], p[6])


def p_funcao_pub_fn_tipo_retorno(p):
    '''funcao : PUB FN ID LPAREN RPAREN tipo_retorno LBRACE RBRACE'''
    p[0] = sa.Funcao_Pub_Fn_Tipo_Retorno(p[1], p[6])
    
def p_funcao_fn_tipo_retorno(p):
    '''funcao : FN ID LPAREN RPAREN tipo_retorno LBRACE RBRACE'''
    p[0] = sa.Funcao_Fn_Tipo_Retorno(p[5])




##### Variavel Tipo_Retorno ######



def p_tipo_retorno(p):
    '''
    tipo_retorno : VOID
                  | I8
                  | U8
                  | I16
                  | U16
                  | I32
                  | U32
                  | I64
                  | U64
                  | I128
                  | U128
    '''
    p[0] = sa.Tipo_Retorno(p[1])
 


##### Variavel Params ######


def p_params_id_tipo_retorno(p):
    
    '''params : ID COLON tipo_retorno'''
    
    p[0] = sa.Params_Id_Tipo_Retorno(p[3])
    
def p_params_id_tipo_retorno_params(p):
    
    '''params : ID COLON tipo_retorno COMMA params'''
    
    p[0] = sa.Params_Id_Tipo_Retorno(p[3],p[5])



##### Variavel Call ######


def p_call_args(p):
    
    '''call : ID LPAREN args RPAREN'''
    
    p[0] = sa.Call_Args(p[3])
    

def p_call_no_args(p):
    
    '''call : ID LPAREN RPAREN'''
    
    p[0] = sa.Call_No_Args()

##### Variavel Args ######



def p_args_id(p):
    '''
    args : ID
    '''
    p[0] = sa.Args_Id()


def p_args_id_args(p):
    '''
    args : ID COMMA args
    '''
    p[0] = sa.Args_Id_Args(p[3])


def p_args_string_args(p):
    '''
    args : STRING COMMA DOT LBRACE args RBRACE
    '''
    p[0] = sa.Args_String_Args(p[3])
    
    
def p_args_string(p):
    '''
    args : STRING COMMA DOT LBRACE  RBRACE
    '''
    p[0] = sa.Args_String()


##### Variavel Decl ######

def p_decl_var_tipo_retorno_expr(p):
    '''
    decl : VAR ID COLON tipo_retorno EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Var_Tipo_Retorno_Expr(p[4], p[6])


def p_decl_const_expr(p):
    '''
    decl : CONST ID EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Const_Expr(p[4])


def p_decl_const_tipo_retorno_expr(p):
    '''
    decl : CONST ID COLON tipo_retorno EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Const_Tipo_Retorno_Expr(p[4], p[6])

def p_decl_equal_expr(p):
    '''
    decl : ID EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Expr(p[3])


def p_decl_expr(p):
    '''
    decl : expr SEMICOLON
    '''
    p[0] = sa.Decl_Expr(p[1])





def p_decl_id_plusequal_expr(p):
    '''
    decl : ID PLUSEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_PlusEqual_Expr(p[3])


def p_decl_id_pluspercent_expr(p):
    '''
    decl : ID PLUSPERCENT expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_PlusPercent_Expr(p[3])


def p_decl_id_pluspercentequal_expr(p):
    '''
    decl : ID PLUSPERCENTEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_PlusPercentEqual_Expr(p[3])


def p_decl_id_pluspipe_expr(p):
    '''
    decl : ID PLUSPIPE expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_PlusPipe_Expr(p[3])



def p_decl_id_pluspipeequal_expr(p):
    '''
    decl : ID PLUSPIPEEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_PlusPipeEqual_Expr(p[3])


def p_decl_id_minusequal_expr(p):
    '''
    decl : ID MINUSEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_MinusEqual_Expr(p[3])


def p_decl_id_minuspercent_expr(p):
    '''
    decl : ID MINUSPERCENT expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_MinusPercent_Expr(p[3])


def p_decl_id_minuspercentequal_expr(p):
    '''
    decl : ID MINUSPERCENTEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_MinusPercentEqual_Expr(p[3])


def p_decl_id_minuspipe_expr(p):
    '''
    decl : ID MINUSPIPE expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_MinusPipe_Expr(p[3])


def p_decl_id_minuspipeequal_expr(p):
    '''
    decl : ID MINUSPIPEEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Id_MinusPipeEqual_Expr(p[3])


##### Variavel Expr ######


def p_expr_builtinidentifier_String(p):
    '''
    expr : BUILTINIDENTIFIER LPAREN STRING RPAREN
    '''
    p[0] = sa.Expr_BuiltinIdentifier_String()

def p_expr_builtinidentifier_expr(p):
    '''
    expr : BUILTINIDENTIFIER LPAREN STRING RPAREN DOT expr
    '''
    p[0] = sa.Expr_BuiltinIdentifier_Expr(p[6])


def p_expr_id_plus_expr(p):
    '''
    expr : ID PLUS expr
    '''
    p[0] = sa.Expr_Id_Plus_Expr(p[3])



def p_expr_id(p):
    '''
    expr : ID
    '''
    p[0] = sa.Expr_Id()


def p_expr_id_expr(p):
    '''
    expr : ID DOT expr
    '''
    p[0] = sa.Expr_Id_Expr(p[3])

def p_expr_call(p):
    '''
    expr : call
    '''
    p[0] = sa.Expr_Call(p[1])

def p_expr_integer(p):
    '''expr : INTEGER'''
    p[0] = sa.Expr_Integer()


def p_expr_id_minus_expr(p):
    '''
    expr : ID MINUS expr
    '''
    p[0] = sa.Expr_Id_Minus_Expr(p[3])


def p_expr_id_slash_expr(p):
    '''
    expr : ID SLASH expr
    '''
    p[0] = sa.Expr_Id_Slash_Expr(p[3])


def p_expr_id_asterisk_expr(p):
    '''
    expr : ID ASTERISK expr
    '''
    p[0] = sa.Expr_Id_Asterisk_Expr(p[3])


def p_expr_id_rarrow_expr(p):
    '''
    expr : ID RARROW expr
    '''
    p[0] = sa.Expr_Id_Rarrow_Expr(p[3])


def p_expr_id_larrow_expr(p):
    '''
    expr : ID LARROW expr
    '''
    p[0] = sa.Expr_Id_Larrow_Expr(p[3])


def p_expr_id_percent_expr(p):
    '''
    expr : ID PERCENT expr
    '''
    p[0] = sa.Expr_Id_Percent_Expr(p[3])



def p_expr_id_equalequal_expr(p):
    '''
    expr : ID EQUALEQUAL expr
    '''
    p[0] = sa.Expr_Id_EqualEqual_Expr(p[3])


def p_expr_id_and_expr(p):
    '''
    expr : ID AND expr
    '''
    p[0] = sa.Expr_Id_And_Expr(p[3])


def p_expr_id_or_expr(p):
    '''
    expr : ID OR expr
    '''
    p[0] = sa.Expr_Id_Or_Expr(p[3])


def p_expr_true(p):
    '''
    expr : TRUE
    '''
    p[0] = sa.Expr_True()

def p_expr_false(p):
    '''
    expr : FALSE
    '''
    p[0] = sa.Expr_False()


##### Variavel Decl_interna ######


def p_decl_interna_break(p):
    '''
    decl_interna : BREAK SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Break()


def p_decl_interna_return_expr(p):
    '''
    decl_interna : RETURN expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Return_Expr(p[2])
    
    
    
def p_decl_interna_while_expr_decl_interna(p):
    '''
    decl_interna : WHILE LPAREN expr RPAREN LBRACE decl_interna RBRACE
    '''
    p[0] = sa.Decl_Interna_While_Expr_Decl_Interna(
        p[3],
        p[6]
    )


def p_decl_interna_for_decl_interna(p):
    '''
    decl_interna : FOR LPAREN INTEGER DOT2 INTEGER RPAREN PIPE ID PIPE LBRACE decl_interna RBRACE
    '''
    p[0] = sa.Decl_Interna_For_Decl_Interna(
        p[11]
    )  
    
def p_decl_interna_expr(p):
    '''decl_interna : expr SEMICOLON'''
    p[0] = sa.Decl_Interna_Expr(p[1])
    
    
def p_decl_interna_if_expr_decl_interna(p):
    '''
    decl_interna : IF LPAREN expr RPAREN LBRACE decl_interna RBRACE
    '''
    p[0] = sa.Decl_Interna_If_Expr_Decl_Interna(
        p[3],
        p[6]
    )
    
    

def p_decl_interna_var_tipo_retorno_expr(p):
    '''
    decl_interna : VAR ID COLON tipo_retorno EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Var_Tipo_Retorno_Expr(p[4], p[6])


def p_decl_interna_const_expr(p):
    '''
    decl_interna : CONST ID EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Const_Expr(p[4])


def p_decl_interna_const_tipo_retorno_expr(p):
    '''
    decl_interna : CONST ID COLON tipo_retorno EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Const_Tipo_Retorno_Expr(p[4], p[6])
    
    
    
def p_decl_interna_var_tipo_retorno_expr_decl_interna(p):
    '''
    decl_interna : VAR ID COLON tipo_retorno EQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(
        p[4],
        p[6],
        p[8]
    )


def p_decl_interna_const_expr_decl_interna(p):
    '''
    decl_interna : CONST ID EQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Const_Expr_Decl_Interna(
        p[4],
        p[6]
    )


def p_decl_interna_const_tipo_retorno_expr_decl_interna(p):
    '''
    decl_interna : CONST ID COLON tipo_retorno EQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(
        p[4],
        p[6],
        p[8]
    )
    
def p_decl_interna_equal_expr(p):
    '''
    decl_interna : ID EQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_Equal_Expr(p[3])


def p_decl_interna_plusequal_expr(p):
    '''
    decl_interna : ID PLUSEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_PlusEqual_Expr(p[3])


def p_decl_interna_pluspercent_expr(p):
    '''
    decl_interna : ID PLUSPERCENT expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_PlusPercent_Expr(p[3])


def p_decl_interna_pluspercentequal_expr(p):
    '''
    decl_interna : ID PLUSPERCENTEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_PlusPercentEqual_Expr(p[3])


def p_decl_interna_pluspipe_expr(p):
    '''
    decl_interna : ID PLUSPIPE expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_PlusPipe_Expr(p[3])
    
    
def p_decl_interna_equal_expr_decl_interna(p):
    '''
    decl_interna : ID EQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Equal_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_plusequal_expr_decl_interna(p):
    '''
    decl_interna : ID PLUSEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_PlusEqual_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_pluspercent_expr_decl_interna(p):
    '''
    decl_interna : ID PLUSPERCENT expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_PlusPercent_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_pluspercentequal_expr_decl_interna(p):
    '''
    decl_interna : ID PLUSPERCENTEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_PlusPercentEqual_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_pluspipe_expr_decl_interna(p):
    '''
    decl_interna : ID PLUSPIPE expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_PlusPipe_Expr_Decl_Interna(p[3], p[5])




def p_decl_interna_pluspipeequal_expr(p):
    '''
    decl_interna : ID PLUSPIPEEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_PlusPipeEqual_Expr(p[3])


def p_decl_interna_minusequal_expr(p):
    '''
    decl_interna : ID MINUSEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_MinusEqual_Expr(p[3])


def p_decl_interna_minuspercent_expr(p):
    '''
    decl_interna : ID MINUSPERCENT expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_MinusPercent_Expr(p[3])


def p_decl_interna_minuspercentequal_expr(p):
    '''
    decl_interna : ID MINUSPERCENTEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_MinusPercentEqual_Expr(p[3])


def p_decl_interna_minuspipe_expr(p):
    '''
    decl_interna : ID MINUSPIPE expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_MinusPipe_Expr(p[3])


def p_decl_interna_minuspipeequal_expr(p):
    '''
    decl_interna : ID MINUSPIPEEQUAL expr SEMICOLON
    '''
    p[0] = sa.Decl_Interna_MinusPipeEqual_Expr(p[3])


def p_decl_interna_pluspipeequal_expr_decl_interna(p):
    '''
    decl_interna : ID PLUSPIPEEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_PlusPipeEqual_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_minusequal_expr_decl_interna(p):
    '''
    decl_interna : ID MINUSEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_MinusEqual_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_minuspercent_expr_decl_interna(p):
    '''
    decl_interna : ID MINUSPERCENT expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_MinusPercent_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_minuspercentequal_expr_decl_interna(p):
    '''
    decl_interna : ID MINUSPERCENTEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_MinusPercentEqual_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_minuspipe_expr_decl_interna(p):
    '''
    decl_interna : ID MINUSPIPE expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_MinusPipe_Expr_Decl_Interna(p[3], p[5])


def p_decl_interna_minuspipeequal_expr_decl_interna(p):
    '''
    decl_interna : ID MINUSPIPEEQUAL expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_MinusPipeEqual_Expr_Decl_Interna(p[3], p[5])

def p_decl_interna_expr_decl_interna(p):
    ''' decl_interna : expr SEMICOLON decl_interna'''
    p[0] = sa.Decl_Interna_Expr_Decl_Interna(p[1])


def p_decl_interna_break_decl_interna(p):
    '''
    decl_interna : BREAK SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Break_Decl_Interna(p[3])


def p_decl_interna_return_expr_decl_interna(p):
    '''
    decl_interna : RETURN expr SEMICOLON decl_interna
    '''
    p[0] = sa.Decl_Interna_Return_Expr_Decl_Interna(
        p[2],
        p[4]
    )


def p_decl_interna_while_expr_decl_interna_decl_interna(p):
    '''
    decl_interna : WHILE LPAREN expr RPAREN LBRACE decl_interna RBRACE decl_interna
    '''
    p[0] = sa.Decl_Interna_While_Expr_Decl_Interna_Decl_Interna(
        p[3],
        p[6],
        p[8]
    )


def p_decl_interna_for_decl_interna_decl_interna(p):
    '''
    decl_interna : FOR LPAREN INTEGER DOT2 INTEGER RPAREN PIPE ID PIPE LBRACE decl_interna RBRACE decl_interna
    '''
    p[0] = sa.Decl_Interna_For_Decl_Interna_Decl_Interna(
        p[11],
        p[13]
    )


def p_decl_interna_if_expr_decl_interna_decl_interna(p):
    '''
    decl_interna : IF LPAREN expr RPAREN LBRACE decl_interna RBRACE decl_interna
    '''
    p[0] = sa.Decl_Interna_If_Expr_Decl_Interna_Decl_Interna(
        p[3],
        p[6],
        p[8]
    )


def main():
    f = open("ex/exemplo.zig", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()