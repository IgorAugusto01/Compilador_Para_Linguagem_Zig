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
    'programa : funcao'
    p[0] = sa.Programa_Funcao(p[1])

# def p_programa_comandos(p):
#     'programa : comandos'
#     p[0] = sa.Programa_Comandos(p[1])

def p_programa_funcao_programa(p):
    'programa : funcao programa'
    p[0] = sa.Programa_Funcao_Programa(p[1], p[2])

# def p_programa_comandos_programa(p):
#     'programa : comandos programa'
#     p[0] = sa.Programa_Comandos_Programa(p[1], p[2])
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
###### REGRAS PARA FUNCAO #######  


def p_funcao_pub_fn_no_params_sem_corpo(p):
    '''funcao : PUB FN ID LPAREN RPAREN tipo_retorno LBRACE RBRACE'''
    
    p[0] = sa.Funcao_Pub_Fn_No_Params_Sem_Corpo(p[7])
    
def p_funcao_fn_no_params_sem_corpo(p):
    '''funcao : FN ID LPAREN RPAREN tipo_retorno LBRACE RBRACE'''
    
    p[0] = sa.Funcao_Fn_No_Params_Sem_Corpo(p[6])
    
def p_funcao_pub_fn_params_sem_corpo(p):
    '''funcao : PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE RBRACE'''
    
    p[0] = sa.Funcao_Pub_Fn_Params_Sem_Corpo(p[5], p[8])

def p_funcao_fn_params_sem_corpo(p):
    '''funcao : FN ID LPAREN params RPAREN tipo_retorno LBRACE RBRACE'''
    
    p[0] = sa.Funcao_Fn_Params_Sem_Corpo(p[4], p[7])

def p_funcao_pub_fn_params_corpo(p):
    '''funcao : PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE'''
    
    p[0] = sa.Funcao_Pub_Fn_Params_Corpo(p[5], p[8], p[10]) 
    
def p_funcao_fn_params_corpo(p):
    '''funcao : FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE'''
    
    p[0] = sa.Funcao_Fn_Params_Corpo(p[4], p[7], p[9])
    
def p_funcao_pub_fn_no_params_corpo(p):
    '''funcao : PUB FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE'''
    
    p[0] = sa.Funcao_Pub_Fn_No_Params_Corpo(p[7], p[9])

def p_funcao_fn_no_params_corpo(p):
    '''funcao : FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE'''
    
    p[0] = sa.Funcao_Fn_No_Params_Corpo(p[6], p[8])






















##### REGRA TIPO_RETORNO #####

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
    '''
    p[0] = sa.Tipo_Retorno(p[1])
    
    
    
    
    
    
    
    
    
 #### REGRAS PARA PARAMS ###### 
def p_params_tipo_retorno(p):
    '''
    params : ID COLON tipo_retorno
    '''
    
    p[0] = sa.Params_Tipo_Retorno(p[3])
    
def p_params_tipo_retorno_params(p):
    '''
    params : ID COLON tipo_retorno COMMA params
    '''
    
    p[0] = sa.Params_Tipo_Retorno_Params(p[3], p[5])
    
    
    
    
    
    
    
    
    
###### REGRAS PARA CORPO #######
    
    
    
def p_corpo_comandos(p):
    '''
    corpo : comandos
    '''
    p[0] = sa.Corpo_Comandos(p[1])
    
    
    
    
###### REGRAS PARA COMANDOS #######
    
def p_comandos_comando(p):
    '''
    comandos : comando
    '''
    p[0] = sa.Comandos_Comando(p[1])
    
def p_comandos_comando_comandos(p):
    '''
    comandos : comando  comandos
    '''
    p[0] = sa.Comandos_Comando_Comandos(p[1], p[2])
    
    
    
    
    
###### REGRAS PARA COMANDO #######

def p_comando_var(p):
    '''
    comando : VAR ID COLON tipo_retorno EQUAL expr SEMICOLON
    '''
    p[0] = sa.Comando_Var(p[4], p[6])
 
def p_comando_const_expr(p):
       
    '''comando : CONST ID EQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Const_Expr(p[4])
    
    
def p_comando_const_tipo_retorno_expr(p):
    '''comando : CONST ID COLON tipo_retorno EQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Const_Tipo_Retorno_Expr(p[4], p[6])   
    
def p_comando_id_equal_expr(p):
    '''comando : ID EQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Equal_Expr(p[3]) 


def p_comando_id_plus_equal_expr(p):
    '''comando : ID PLUSEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Plus_Equal_Expr(p[3])  
    
def p_comando_id_plus_percent_expr(p):
    '''comando : ID PLUSPERCENT expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Plus_Percent_Expr(p[3])

def p_comando_id_plus_percent_equal_expr(p):
    '''comando : ID PLUSPERCENTEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Plus_Percent_Equal_Expr(p[3])

def p_comando_id_plus_pipe_expr(p):
    '''comando : ID PLUSPIPE expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Plus_Pipe_Expr(p[3])
    
def p_comando_id_plus_pipe_equal_expr(p):
    '''comando : ID PLUSPIPEEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Plus_Pipe_Equal_Expr(p[3])
    

def p_comando_id_minus_equal_expr(p):
    '''comando : ID MINUSEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Minus_Equal_Expr(p[3])

def p_comando_id_minus_percent_expr(p):
    '''comando : ID MINUSPERCENT expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Minus_Percent_Expr(p[3])

def p_comando_id_minus_percent_equal_expr(p):
    '''comando : ID MINUSPERCENTEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Minus_Percent_Equal_Expr(p[3])

def p_comando_id_minus_pipe_expr(p):
    '''comando : ID MINUSPIPE expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Minus_Pipe_Expr(p[3])

def p_comando_id_minus_pipe_equal_expr(p):
    '''comando : ID MINUSPIPEEQUAL expr SEMICOLON'''
    
    p[0] = sa.Comando_Id_Minus_Pipe_Equal_Expr(p[3])
    
def p_comando_while(p):
    '''comando : WHILE LPAREN expr RPAREN LBRACE comandos RBRACE'''
    
    p[0] = sa.Comando_While(p[3], p[6])

def p_comando_for(p):
    '''comando : FOR LPAREN comando INTEGER DOT2 INTEGER RPAREN LBRACE comandos RBRACE'''
    
    p[0] = sa.Comando_For(p[3], p[4], p[6], p[9])
    
def p_comando_return(p):
    '''comando : RETURN expr SEMICOLON'''
    
    p[0] = sa.Comando_Return(p[2])

def p_comando_if(p):
    '''comando : IF LPAREN expr RPAREN LBRACE comandos RBRACE'''
    
    p[0] = sa.Comando_If(p[3], p[6])

def p_comando_break(p):
    '''comando : BREAK SEMICOLON'''
    
    p[0] = sa.Comando_Break(p[1])
    

    
#### REGRAS PARA EXPR ####


def p_expr_id(p):
    '''expr : ID'''
    
    p[0] = sa.Expr_Id(p[1])

def p_expr_id_expr(p):
    '''x : ID DOT expr'''
    
    p[0] = sa.Expr_Id_Expr(p[1], p[3])
    
def p_expr_integer(p):
    '''x : INTEGER'''
    
    p[0] = sa.Expr_Integer(p[1])
    
def p_expr_char(p):
    '''x : CHAR'''
    
    p[0] = sa.Expr_Char(p[1])

def p_expr_string(p):
    '''x : STRING'''
    
    p[0] = sa.Expr_String(p[1])

def p_expr_builtin_identifier(p):
    '''x : BUILTINIDENTIFIER LPAREN expr RPAREN'''
    
    p[0] = sa.Expr_Builtin_Identifier(p[3])

def p_expr_builtin_identifier_expr(p):
    '''x : BUILTINIDENTIFIER LPAREN expr RPAREN DOT expr'''
    
    p[0] = sa.Expr_Builtin_Identifier_Expr(p[3], p[6])
    

def p_expr_plus_expr(p):
    '''x : expr PLUS expr'''
    
    p[0] = sa.Expr_Plus_Expr(p[1], p[3])

def p_expr_minus_expr(p):
    '''x : expr MINUS expr'''
    
    p[0] = sa.Expr_Minus_Expr(p[1], p[3])

def p_expr_div_expr(p):
    '''x : expr SLASH expr'''
    
    p[0] = sa.Expr_Div_Expr(p[1], p[3])

def p_expr_mult_expr(p):
    '''x : expr ASTERISK expr'''
    
    p[0] = sa.Expr_Mult_Expr(p[1], p[3])
    

def p_expr_rarrow_expr(p):
    '''x : expr RARROW expr'''
    
    p[0] = sa.Expr_Rarrow_Expr(p[1], p[3])

def p_expr_larrow_expr(p):
    '''x : expr LARROW expr'''
    p[0] = sa.Expr_Larrow_Expr(p[1], p[3])

def p_expr_mod_expr(p):
    '''x : expr PERCENT expr'''
    p[0] = sa.Expr_Mod_Expr(p[1], p[3])

def p_expr_equal_equal_expr(p):
    '''x : expr EQUALEQUAL expr'''
    p[0] = sa.Expr_Equal_Equal_Expr(p[1], p[3])

def p_expr_and_expr(p):
    '''x : expr AND expr'''
    p[0] = sa.Expr_And_Expr(p[1], p[3])

def p_expr_or_expr(p):
    '''x : expr OR expr'''
    p[0] = sa.Expr_Or_Expr(p[1], p[3])

def p_expr_true(p):
    '''x : TRUE'''
    p[0] = sa.Expr_True(p[1])

def p_expr_false_expr(p):
    '''x : FALSE'''
    p[0] = sa.Expr_False(p[1]) 

def p_expr_call(p):
    '''x : call'''
    p[0] = sa.Expr_Call(p[1])  
    
    
def p_call_expr_args(p):
    '''call : expr LPAREN args RPAREN'''
    p[0] = sa.Call_Expr_Args(p[1], p[3])

def p_call_expr_no_args(p):
    '''call : expr LPAREN RPAREN'''
    p[0] = sa.Call_Expr_No_Args(p[1])

def p_call_expr_args1_args2(p):
    '''call : expr LPAREN args  COMMA DOT LBRACE args RBRACE RPAREN'''
    p[0] = sa.Call_Expr_Args1_Args2(p[1], p[3], p[7])
    
def p_call_expr_arg1_no_args2(p):
    '''call : expr LPAREN args  COMMA DOT LBRACE RPAREN'''
    p[0] = sa.Call_Expr_Arg1_No_Args2(p[1], p[3])
    
    
    
    
    
###### REGRAS PARA ARGS #########

def p_args_expr_args(p):
    '''args : expr COMMA args'''
    
    p[0] = sa.Args_Expr_Args(p[1],p[3])

def p_args_exp(p):
    '''args : expr'''
    
    p[0] = sa.Args_Expr(p[1])
    
    

def main():
    f = open("ex/exemplo.zig", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()