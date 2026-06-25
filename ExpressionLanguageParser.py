import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa




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


























def main():
    f = open("ex/exemplo.zig", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()