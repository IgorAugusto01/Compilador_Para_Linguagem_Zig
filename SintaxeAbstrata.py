from abc import abstractmethod
from abc import ABC



###################### DEFINIÇÃO DA CLASSE ABSTRATA PROGRAMA  #########################

class ProgramaAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass


class Programa_Funcao(ProgramaAbstract):
    def __init__(self, funcao):
        self.funcao = funcao

    def accept(self,visitor):
       return visitor.visitPrograma_Funcao(self)

class Programa_Comandos(ProgramaAbstract):
    def __init__(self,comandos):
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitPrograma_Comandos(self)
    
class Programa_Funcao_Programa(ProgramaAbstract):
    def __init__(self,funcao,programa):
        self.funcao = funcao
        self.programa = programa

    def accept(self,visitor):
        return visitor.visitPrograma_Funcao_Programa(self)

class Programa_Comandos_Programa(ProgramaAbstract):
    def __init__(self,comandos,programa):
        self.comandos = comandos
        self.programa = programa

    def accept(self,visitor):
        return visitor.visitPrograma_Comandos_Programa(self)
    
    

   
###################### DEFINIÇÃO DA CLASSE ABSTRATA FUNCAO  #########################



class FuncaoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# funcao -> PUB FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE

class Funcao_Pub_Fn_Params(FuncaoAbstract):
    def __init__(self, ID, params, tipo_retorno, corpo):
        self.ID = ID
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn_Params(self)


# funcao -> PUB FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE

class Funcao_Pub_Fn(FuncaoAbstract):
    def __init__(self, ID, tipo_retorno, corpo):
        self.ID = ID
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn(self)


# funcao -> FN ID LPAREN params RPAREN tipo_retorno LBRACE corpo RBRACE

class Funcao_Fn_Params(FuncaoAbstract):
    def __init__(self, ID, params, tipo_retorno, corpo):
        self.ID = ID
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self, visitor):
        return visitor.visitFuncao_Fn_Params(self)


# funcao -> FN ID LPAREN RPAREN tipo_retorno LBRACE corpo RBRACE

class Funcao_Fn(FuncaoAbstract):
    def __init__(self, ID, tipo_retorno, corpo):
        self.ID = ID
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self, visitor):
        return visitor.visitFuncao_Fn(self)

###################### DEFINIÇÃO DA CLASSE ABSTRATA COMANDOS  #########################


class ComandosAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
    
    
    
    
class Comandos_Comando(ComandosAbstract):
    def __init__(self, comando):
        self.comando = comando

    def accept(self, visitor):
        return visitor.visitComandos_Comando(self)
    
    
class Comandos_Comando_Comandos(ComandosAbstract):
    def __init__(self, comando, comandos):
        self.comando = comando
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitComandos_Comando_Comandos(self)
    
    
    
    
    
 ###################### DEFINIÇÃO DA CLASSE ABSTRATA TIPO_RETORNO E SUAS CLASSES CONCRETAS #########################

    
class TipoRetornoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass 
    
class TipoRetorno_Void(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_Void(self)


class TipoRetorno_I8(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_I8(self)


class TipoRetorno_U8(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_U8(self)


class TipoRetorno_I16(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_I16(self)


class TipoRetorno_U16(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_U16(self)


class TipoRetorno_I32(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_I32(self)


class TipoRetorno_U32(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_U32(self)


class TipoRetorno_I64(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_I64(self)


class TipoRetorno_U64(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_U64(self)


class TipoRetorno_I128(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_I128(self)


class TipoRetorno_U128(TipoRetornoAbstract):

    def accept(self, visitor):
        return visitor.visitTipoRetorno_U128(self)
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA PARAMS E SUAS CLASSES CONCRETAS #########################

class ParamsAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# params -> ID COLON tipo_retorno

class Params_ID_TipoRetorno(ParamsAbstract):
    def __init__(self, ID, tipo_retorno):
        self.ID = ID
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitParams_ID_TipoRetorno(self)


# params -> ID COLON tipo_retorno COMMA params

class Params_ID_TipoRetorno_Params(ParamsAbstract):
    def __init__(self, ID, tipo_retorno, params):
        self.ID = ID
        self.tipo_retorno = tipo_retorno
        self.params = params

    def accept(self, visitor):
        return visitor.visitParams_ID_TipoRetorno_Params(self)
    
    
    
    
    ###################### DEFINIÇÃO DA CLASSE ABSTRATA CORPO E SUAS CLASSES CONCRETAS #########################

class CorpoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
    
    
    
class Corpo_Comandos(CorpoAbstract):
    def __init__(self, comandos):
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitCorpo_Comandos(self)
    
    
    
    
#### DEFINICAO DA CLASSE COMANDO ###############


class ComandoAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Comando_ID_TipoRetorno_Expr(ComandoAbstract):

    def __init__(self, id, tipo_retorno, expr):
        self.id = id
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_TipoRetorno_Expr(self)


class Comando_ID_Expr(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr(self)


class Comando_ID_TipoRetorno_Expr_2(ComandoAbstract):

    def __init__(self, id, tipo_retorno, expr):
        self.id = id
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_TipoRetorno_Expr_2(self)


class Comando_ID_TipoRetorno_Expr_3(ComandoAbstract):

    def __init__(self, id, tipo_retorno, expr):
        self.id = id
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_TipoRetorno_Expr_3(self)


class Comando_ID_Expr_2(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_2(self)


class Comando_ID_TipoRetorno_Expr_4(ComandoAbstract):

    def __init__(self, id, tipo_retorno, expr):
        self.id = id
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_TipoRetorno_Expr_4(self)


class Comando_Expr(ComandoAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_Expr(self)


class Comando_Expr_Comandos(ComandoAbstract):

    def __init__(self, expr, comandos):
        self.expr = expr
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitComando_Expr_Comandos(self)

class Comando_ID_Expr_3(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_3(self)


class Comando_ID_Expr_4(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_4(self)


class Comando_ID_Expr_5(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_5(self)


class Comando_ID_Expr_6(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_6(self)


class Comando_ID_Expr_7(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_7(self)


class Comando_ID_Expr_8(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_8(self)


class Comando_ID_Expr_9(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_9(self)


class Comando_ID_Expr_10(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_10(self)


class Comando_ID_Expr_11(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_11(self)


class Comando_ID_Expr_12(ComandoAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_ID_Expr_12(self)


class Comando_Expr_Comandos(ComandoAbstract):

    def __init__(self, expr, comandos):
        self.expr = expr
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitComando_Expr_Comandos(self)


class Comando_Expr_Expr(ComandoAbstract):

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self, visitor):
        return visitor.visitComando_Expr_Expr(self)


class Comando_Expr_13(ComandoAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitComando_Expr_13(self)
    
    
    
class Comando_For(ComandoAbstract):

    def __init__(self, expr_inicio, expr_fim, id, comandos):
        self.expr_inicio = expr_inicio
        self.expr_fim = expr_fim
        self.id = id
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitComando_For(self)
    
    
    
    
    
    
    
     
class ExprAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Expr_ID(ExprAbstract):

    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitExpr_ID(self)


class Expr_ID_Expr(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr(self)


class Expr_INTEGER(ExprAbstract):

    def __init__(self, integer):
        self.integer = integer

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER(self)


class Expr_CHAR(ExprAbstract):

    def __init__(self, char):
        self.char = char

    def accept(self, visitor):
        return visitor.visitExpr_CHAR(self)


class Expr_STRING(ExprAbstract):

    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        return visitor.visitExpr_STRING(self)


class Expr_BUILTINIDENTIFIER_STRING(ExprAbstract):

    def __init__(self, builtinidentifier, string):
        self.builtinidentifier = builtinidentifier
        self.string = string

    def accept(self, visitor):
        return visitor.visitExpr_BUILTINIDENTIFIER_STRING(self)


class Expr_BUILTINIDENTIFIER_STRING_Expr(ExprAbstract):

    def __init__(self, builtinidentifier, string, expr):
        self.builtinidentifier = builtinidentifier
        self.string = string
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_BUILTINIDENTIFIER_STRING_Expr(self)


class Expr_INTEGER_Expr(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr(self)


class Expr_INTEGER_Expr_2(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr_2(self)


class Expr_INTEGER_Expr_3(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr_3(self)


class Expr_INTEGER_Expr_4(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr_4(self)


class Expr_INTEGER_Expr_5(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr_5(self)


class Expr_INTEGER_Expr_6(ExprAbstract):

    def __init__(self, integer, expr):
        self.integer = integer
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_INTEGER_Expr_6(self)


class Expr_ID_Expr_2(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_2(self)


class Expr_ID_Expr_3(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_3(self)


class Expr_ID_Expr_4(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_4(self)


class Expr_ID_Expr_5(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_5(self)


class Expr_ID_Expr_6(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_6(self)


class Expr_ID_Expr_7(ExprAbstract):

    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_ID_Expr_7(self)


class Expr_True(ExprAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitExpr_True(self)


class Expr_False(ExprAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitExpr_False(self)


class Expr_Call(ExprAbstract):

    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitExpr_Call(self)
    
    
class Expr_Call_Expr(ExprAbstract):

    def __init__(self, call, expr):
        self.call = call
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Call_Expr(self)



class CallAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ArgsAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# AST

class Call_ID_ID(CallAbstract):

    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def accept(self, visitor):
        return visitor.visitCall_ID_ID(self)


class Call_ID_ID_Args(CallAbstract):

    def __init__(self, id1, id2, args):
        self.id1 = id1
        self.id2 = id2
        self.args = args

    def accept(self, visitor):
        return visitor.visitCall_ID_ID_Args(self)


class Call_ID_ID_ID(CallAbstract):

    def __init__(self, id1, id2, id3):
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3

    def accept(self, visitor):
        return visitor.visitCall_ID_ID_ID(self)


class Call_ID_ID_ID_Args(CallAbstract):

    def __init__(self, id1, id2, id3, args):
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.args = args

    def accept(self, visitor):
        return visitor.visitCall_ID_ID_ID_Args(self)

class Args_Expr_Args(ArgsAbstract):

    def __init__(self, expr, args):
        self.expr = expr
        self.args = args

    def accept(self, visitor):
        return visitor.visitArgs_Expr_Args(self)


class Args_Expr(ArgsAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitArgs_Expr(self)