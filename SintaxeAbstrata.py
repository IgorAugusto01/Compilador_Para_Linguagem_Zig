from abc import abstractmethod
from abc import ABC



###################### DEFINIÇÃO DA CLASSE ABSTRATA PROGRAMA E SUAS CLASSES CONCRETAS #########################

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
    


































###################### DEFINIÇÃO DA CLASSE ABSTRATA FUNCAO E SUAS CLASSES CONCRETAS  #########################

class FuncaoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass
   
class Funcao_Pub_Fn_Params_Corpo(FuncaoAbstract):
    def __init__(self,params, tipo_retorno, corpo):
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self,visitor):
        return visitor.visitFuncao_Pub_Fn_Params_Corpo(self)
    
    
class Funcao_Pub_Fn_Params_Sem_Corpo(FuncaoAbstract):
    def __init__(self,params, tipo_retorno):
        self.params = params
        self.tipo_retorno = tipo_retorno
       

    def accept(self,visitor):
        return visitor.visitFuncao_Pub_Fn_Params_Sem_Corpo(self)

class Funcao_Pub_Fn_No_Params_Corpo(FuncaoAbstract):
    def __init__(self, tipo_retorno, corpo):
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self,visitor):
        return visitor.visitFuncao_Pub_Fn_No_Params_Corpo(self)
    
    
class Funcao_Pub_Fn_No_Params_Sem_Corpo(FuncaoAbstract):
    def __init__(self, tipo_retorno):
        self.tipo_retorno = tipo_retorno

    def accept(self,visitor):
        return visitor.visitFuncao_Pub_Fn_No_Params_Sem_Corpo(self)
    
    
class Funcao_Fn_Params_Corpo(FuncaoAbstract):
    def __init__(self,params, tipo_retorno, corpo):
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self,visitor):
        return visitor.visitFuncao_Fn_Params_Corpo(self)
    
    
    
    
    
class Funcao_Fn_Params_Sem_Corpo(FuncaoAbstract):
    def __init__(self,params, tipo_retorno):
        self.params = params
        self.tipo_retorno = tipo_retorno
        

    def accept(self,visitor):
        return visitor.visitFuncao_Fn_Params_Sem_Corpo(self)

    def accept(self,visitor):
        return visitor.visitFuncao_Fn_Params_Corpo(self)
    
class Funcao_Fn_No_Params_Corpo(FuncaoAbstract):
    def __init__(self, tipo_retorno, corpo):
        self.tipo_retorno = tipo_retorno
        self.corpo = corpo

    def accept(self,visitor):
        return visitor.visitFuncao_Fn_No_Params_Corpo(self)
  
class Funcao_Fn_No_Params_Sem_Corpo(FuncaoAbstract):
    def __init__(self, tipo_retorno):
        self.tipo_retorno = tipo_retorno

    def accept(self,visitor):
        return visitor.visitFuncao_Fn_No_Params_Sem_Corpo(self)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA TIPO_RETORNO E SUAS CLASSES CONCRETAS  #########################



class Tipo_RetornoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass

class Tipo_Retorno(Tipo_RetornoAbstract):
    def __init__(self,tipo):
        self.tipo = tipo
        pass

    def accept(self,visitor):
        return visitor.visitTipo_Retorno(self)
    
    
    
    
    
    
    
    
    
    
    
    


###################### DEFINIÇÃO DA CLASSE ABSTRATA PARAMS E SUAS CLASSES CONCRETAS  #########################




class ParamsAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass
   
class Params_Tipo_Retorno(ParamsAbstract):
    def __init__(self, tipo_retorno):
        self.tipo_retorno = tipo_retorno

    def accept(self,visitor):
        return visitor.visitParams_Tipo_Retorno(self)
    
    
class Params_Tipo_Retorno_Params(ParamsAbstract):
    def __init__(self,tipo_retorno, params):
        self.tipo_retorno = tipo_retorno
        self.params = params

    def accept(self,visitor):
        return visitor.visitParams_Tipo_Retorno_Params(self)
   
   
   
   
   
   
   
   
   
   
###################### DEFINIÇÃO DA CLASSE ABSTRATA CORPO E SUAS CLASSES CONCRETAS  ######################## 
    
class CorpoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass
   
class Corpo_Comandos(CorpoAbstract):
    def __init__(self,comandos):
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitCorpo_Comandos(self)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA COMANDOS E SUAS CLASSES CONCRETAS  ######################## 
    
    
class ComandosAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass

class Comandos_Comando(ComandosAbstract):
    def __init__(self,comando):
        self.comando = comando

    def accept(self,visitor):
        return visitor.visitComandos_Comando(self) 
    
class Comandos_Comando_Comandos(ComandosAbstract):
    def __init__(self,comando, comandos):
        self.comando = comando
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitComandos_Comando_Comandos(self)  
    




































###################### DEFINIÇÃO DA CLASSE ABSTRATA COMANDO E SUAS CLASSES CONCRETAS  ######################## 


class ComandoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass
   
class Comando_Var(ComandoAbstract):
    def __init__(self,tipo_retorno,expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Var(self)
    
    
class Comando_Const_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Const_Expr(self)

class Comando_Const_Tipo_Retorno_Expr(ComandoAbstract):
    def __init__(self,tipo_retorno,expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Const_Tipo_Retorno_Expr(self)
    
class Comando_Id_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Equal_Expr(self)


class Comando_Id_Plus_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Plus_Equal_Expr(self)
    
class Comando_Id_Plus_Percent_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Plus_Percent_Expr(self)

class Comando_Id_Plus_Percent_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Plus_Percent_Equal_Expr(self)
    
class Comando_Id_Plus_Pipe_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Plus_Pipe_Expr(self)

class Comando_Id_Plus_Pipe_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Plus_Pipe_Equal_Expr(self)
    
    
class Comando_Id_Minus_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Minus_Equal_Expr(self)

class Comando_Id_Minus_Percent_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Minus_Percent_Expr(self)

class Comando_Id_Minus_Percent_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Minus_Percent_Equal_Expr(self)

class Comando_Id_Minus_Pipe_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Minus_Pipe_Expr(self)

class Comando_Id_Minus_Pipe_Equal_Expr(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Id_Minus_Pipe_Equal_Expr(self)

class Comando_While(ComandoAbstract):
    def __init__(self,expr,comandos):
        self.expr = expr
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitComando_While(self)

class Comando_For(ComandoAbstract):
    def __init__(self,expr,comandos):
        self.expr = expr
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitComando_For(self)

class Comando_Return(ComandoAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitComando_Return(self)

class Comando_If(ComandoAbstract):
    def __init__(self,expr,comandos):
        self.expr = expr
        self.comandos = comandos

    def accept(self,visitor):
        return visitor.visitComando_If(self)
    
class Comando_Break(ComandoAbstract):
    def __init__(self,break_id):
        self.break_id = break_id

    def accept(self,visitor):
        return visitor.visitComando_Break(self)
    
    
    
    
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA EXPR E SUAS CLASSES CONCRETAS  ########################


class ExprAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass
   
class Expr_Id(ExprAbstract):
    def __init__(self,id):
        self.id = id
    

    def accept(self,visitor):
        return visitor.visitExpr_Id(self)

class Expr_Id_Expr(ExprAbstract):
    def __init__(self,id,expr):
        self.id = id
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitExpr_Id_Expr(self)

class Expr_Integer(ExprAbstract):
    def __init__(self,integer):
        self.integer = integer

    def accept(self,visitor):
        return visitor.visitExpr_Integer(self)
    

class Expr_Char(ExprAbstract):
    def __init__(self,char):
        self.char = char

    def accept(self,visitor):
        return visitor.visitExpr_Char(self)
    
class Expr_String(ExprAbstract):
    def __init__(self,string):
        self.string = string

    def accept(self,visitor):
        return visitor.visitExpr_String(self)
    
class Expr_Builtin_Identifier(ExprAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitExpr_Builtin_Identifier(self)

class Expr_Builtin_Identifier_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Builtin_Identifier_Expr(self)
    
class Expr_Plus_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Plus_Expr(self)
class Expr_Minus_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Minus_Expr(self)
    
class Expr_Div_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Div_Expr(self)
    
class Expr_Mult_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Mult_Expr(self)

class Expr_Rarrow_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Rarrow_Expr(self)

class Expr_Larrow_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Larrow_Expr(self)

class Expr_Mod_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Mod_Expr(self)

class Expr_Equal_Equal_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Equal_Equal_Expr(self)

class Expr_And_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_And_Expr(self)

class Expr_Or_Expr(ExprAbstract):
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self,visitor):
        return visitor.visitExpr_Or_Expr(self)

class Expr_True(ExprAbstract):
    def __init__(self,true):
        self.true = true

    def accept(self,visitor):
        return visitor.visitExpr_True(self)

class Expr_False(ExprAbstract):
    def __init__(self,false):
        self.false = false

    def accept(self,visitor):
        return visitor.visitExpr_False(self)

class Expr_Call(ExprAbstract):
    def __init__(self,call):
        self.call = call

    def accept(self,visitor):
        return visitor.visitExpr_Call(self)


###################### DEFINIÇÃO DA CLASSE ABSTRATA CALL E SUAS CLASSES CONCRETAS  ########################


class CallAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass

class Call_Expr_Args(CallAbstract):
    def __init__(self,expr,args):
        self.expr = expr
        self.args = args

    def accept(self,visitor):
        return visitor.visitCall_Expr_Args(self)

class Call_Expr_No_Args(CallAbstract):
    def __init__(self,expr):
        self.expr = expr

    def accept(self,visitor):
        return visitor.visitCall_Expr_No_Args(self)

class Call_Expr_Args1_Args2(CallAbstract):
    def __init__(self,expr,args1,args2):
        self.expr = expr
        self.args1 = args1
        self.args2 = args2

    def accept(self,visitor):
        return visitor.visitCall_Expr_Args1_Args2(self)

class Call_Expr_Args1_No_Args2(CallAbstract):
    def __init__(self,expr,args1):
        self.expr = expr
        self.args1 = args1

    def accept(self,visitor):
        return visitor.visitCall_Expr_Args1_No_Args2(self)
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA ARGS E SUAS CLASSES CONCRETAS  ########################

class ArgsAbstract(ABC):
   @abstractmethod
   def accept(self, visitor):
    pass

class Args_Expr_Args(ArgsAbstract):
    def __init__(self,expr,args):
     self.expr = expr
     self.args = args
     
    def accept(self,visitor):
        return visitor.visitArgs_Expr_Args(self)

class Args_Expr(ArgsAbstract):
    def __init__(self,expr,):
     self.expr = expr
    
     
    def accept(self,visitor):
        return visitor.visitArgs_Expr(self)

        
    