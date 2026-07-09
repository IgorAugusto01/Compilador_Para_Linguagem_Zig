from abc import abstractmethod
from abc import ABC



###################### DEFINIÇÃO DA CLASSE ABSTRATA PROGRAMA E SUAS CLASSES CONCRETAS #########################

class ProgramaAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
       pass

class Programa_Funcao(ProgramaAbstract):
    def __init__(self,funcao):
        self.funcao = funcao
    
    def accept(self,visitor):
        return visitor.visitPrograma_Funcao(self)

        
class Programa_Decl(ProgramaAbstract):
    def __init__(self,decl):
        self.decl = decl
    
    def accept(self,visitor):
        return visitor.visitPrograma_Decl(self)
    
    
class Programa_Funcao_Programa(ProgramaAbstract):
    
    def __init__(self,funcao,programa):
        self.funcao = funcao
        self.programa = programa
    
    def accept(self,visitor):
        return visitor.visitPrograma_Funcao_Programa(self)


class Programa_Decl_Programa(ProgramaAbstract):
    
    def __init__(self,decl,programa):
        self.decl = decl
        self.programa = programa
    
    def accept(self,visitor):
        return visitor.visitPrograma_Decl_Programa(self)
    
####################################################################################################
    
    
    
    
###################### DEFINIÇÃO DA CLASSE ABSTRATA FUNCAO E SUAS CLASSES CONCRETAS #########################    
    
    
    
    
class FuncaoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
      pass
  
  
class Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(FuncaoAbstract):
    def __init__(self, pub, params, tipo_retorno, decl_interna):
        self.pub = pub
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(self)


class Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna(FuncaoAbstract):
    def __init__(self, pub, tipo_retorno, decl_interna):
        self.pub = pub
        self.tipo_retorno = tipo_retorno
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn_Tipo_Retorno_Decl_Interna(self)


class Funcao_Fn_Params_Tipo_Retorno_Decl_Interna(FuncaoAbstract):
    def __init__(self, params, tipo_retorno, decl_interna):
        self.params = params
        self.tipo_retorno = tipo_retorno
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitFuncao_Fn_Params_Tipo_Retorno_Decl_Interna(self)


class Funcao_Fn_Tipo_Retorno_Decl_Interna(FuncaoAbstract):
    def __init__(self, tipo_retorno, decl_interna):
        self.tipo_retorno = tipo_retorno
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitFuncao_Fn_Tipo_Retorno_Decl_Interna(self)


class Funcao_Pub_Fn_Params_Tipo_Retorno(FuncaoAbstract):
    def __init__(self, pub, params, tipo_retorno):
        self.pub = pub
        self.params = params
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn_Params_Tipo_Retorno(self)


class Funcao_Pub_Fn_Tipo_Retorno(FuncaoAbstract):
    def __init__(self, pub, tipo_retorno):
        self.pub = pub
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitFuncao_Pub_Fn_Tipo_Retorno(self)


class Funcao_Fn_Params_Tipo_Retorno(FuncaoAbstract):
    def __init__(self, params, tipo_retorno):
        self.params = params
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitFuncao_Fn_Params_Tipo_Retorno(self)


class Funcao_Fn_Tipo_Retorno(FuncaoAbstract):
    def __init__(self, tipo_retorno):
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitFuncao_Fn_Tipo_Retorno(self)
    
    
####################################################################################################



 ###################### DEFINIÇÃO DA CLASSE ABSTRATA TIPO_RETORNO E SUAS CLASSES CONCRETAS #########################
    
    
class Tipo_RetornoAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Tipo_Retorno(Tipo_RetornoAbstract):
    def __init__(self, tipo):
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitTipo_Retorno(self)
    
 ####################################################################################################
 
 
 
 ###################### DEFINIÇÃO DA CLASSE ABSTRATA PARAMS E SUAS CLASSES CONCRETAS #########################   
    
    
    
class ParamsAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Params_Id_Tipo_Retorno(ParamsAbstract):
    def __init__(self, tipo_retorno):
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitParams_IdTipo_Retorno(self)
    
    
class Params_Id_Tipo_Retorno_Params(ParamsAbstract):
    def __init__(self, tipo_retorno,params):
        self.tipo_retorno = tipo_retorno
        self.params = params
    
    def accept(self, visitor):
        return visitor.visitParams_IdTipo_Retorno_Params(self)
    
    
    
    
    ####################################################################################################
    
     ###################### DEFINIÇÃO DA CLASSE ABSTRATA Call E SUAS CLASSES CONCRETAS ######################### 
     
     
     
     
class CallAbstract(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class Call_Args(CallAbstract):
    
    def __init__(self,args):
        self.args = args
    
    
    def accept(self, visitor):
        return visitor.visitCall_Args(self)

class Call_No_Args(CallAbstract):
    
    def __init__(self):
        pass
    
    
    def accept(self, visitor):
        return visitor.visitCall_No_Args(self)
        
        
        
   
 ####################################################################################################        
        
        
 ###################### DEFINIÇÃO DA CLASSE ABSTRATA ARGS E SUAS CLASSES CONCRETAS ######################### 
 
 
class ArgsAbstract(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class Args_Id(ArgsAbstract):
    
    def __init__(self):
        pass
    
    
    def accept(self, visitor):
        return visitor.visitArgs_Id(self)
 
 
class Args_Id_Args(ArgsAbstract):
    
    def __init__(self,args):
        self.args = args
        
    
    
    def accept(self, visitor):
        return visitor.visitArgs_Id_Args(self)
    
class Args_String_Args(ArgsAbstract):
    
    def __init__(self,args):
       self.args = args
        
    
    
    def accept(self, visitor):
        return visitor.visitArgs_String_Args(self)

class Args_String(ArgsAbstract):
    
    def __init__(self):
      pass
        
    
    
    def accept(self, visitor):
        return visitor.visitArgs_String(self)
    
####################################################################################################  



###################### DEFINIÇÃO DA CLASSE ABSTRATA DECL E SUAS CLASSES CONCRETAS #########################




class DeclAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Decl_Var_Tipo_Retorno_Expr(DeclAbstract):

    def __init__(self, tipo_retorno, expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Var_Tipo_Retorno_Expr(self)
    
    
class Decl_Const_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Const_Expr(self)

class Decl_Const_Tipo_Retorno_Expr(DeclAbstract):

    def __init__(self, tipo_retorno, expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Const_Tipo_Retorno_Expr(self)

class Decl_Equal_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Equal_Expr(self)
    
class Decl_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Expr(self)
    
    
class Decl_Id_PlusEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_PlusEqual_Expr(self)
    
    
class Decl_Id_PlusPercent_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_PlusPercent_Expr(self)
    
class Decl_Id_PlusPercentEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_PlusPercentEqual_Expr(self)

class Decl_Id_PlusPipe_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_PlusPipe_Expr(self)
    
    
class Decl_Id_PlusPipeEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_PlusPipeEqual_Expr(self)


class Decl_Id_MinusEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_MinusEqual_Expr(self)


class Decl_Id_MinusPercent_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_MinusPercent_Expr(self)


class Decl_Id_MinusPercentEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_MinusPercentEqual_Expr(self)
    
class Decl_Id_MinusPipe_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_MinusPipe_Expr(self)


class Decl_Id_MinusPipeEqual_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Id_MinusPipeEqual_Expr(self)
####################################################################################################  



###################### DEFINIÇÃO DA CLASSE ABSTRATA EXPR E SUAS CLASSES CONCRETAS #########################  
    
    
    
class ExprAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass   



class Expr_BuiltinIdentifier_String(ExprAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitExpr_BuiltinIdentifier_Expr(self)
    
    
class Expr_BuiltinIdentifier_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_BuiltinIdentifier_Expr(self)

class Expr_Id_Plus_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Expr(self)

class Expr_Id(ExprAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitExpr_Id(self)


class Expr_Id_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Expr(self)

class Expr_Call(ExprAbstract):

    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitExpr_Id_Expr(self)

class Expr_Integer(ExprAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitExpr_Integer(self)
    

class Expr_Id_Minus_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Minus_Expr(self)


class Expr_Id_Slash_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Slash_Expr(self)


class Expr_Id_Asterisk_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Asterisk_Expr(self)


class Expr_Id_Rarrow_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Greater_Expr(self)


class Expr_Id_Larrow_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Less_Expr(self)


class Expr_Id_Percent_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Percent_Expr(self)

class Expr_Id_EqualEqual_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_EqualEqual_Expr(self)


class Expr_Id_And_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_And_Expr(self)


class Expr_Id_Or_Expr(ExprAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpr_Id_Or_Expr(self)
    
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
    
####################################################################################################  



###################### DEFINIÇÃO DA CLASSE ABSTRATA DECL_INTERNA E SUAS CLASSES CONCRETAS #########################  

from abc import ABC, abstractmethod


class Decl_InternaAbstract(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Decl_Interna_Break(Decl_InternaAbstract):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Break(self)


class Decl_Interna_Return_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Return_Expr(self)

class Decl_Interna_While_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_While_Expr_Decl_Interna(self)


class Decl_Interna_For_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, decl_interna):
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_For_Decl_Interna(self)
    
class Decl_Interna_Expr(DeclAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl__Interna_Expr(self)

class Decl_Interna_If_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_If_Expr_Decl_Interna(self)

class Decl_Interna_Var_Tipo_Retorno_Expr(Decl_InternaAbstract):

    def __init__(self, tipo_retorno, expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Var_Tipo_Retorno_Expr(self)


class Decl_Interna_Const_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Const_Expr(self)


class Decl_Interna_Const_Tipo_Retorno_Expr(Decl_InternaAbstract):

    def __init__(self, tipo_retorno, expr):
        self.tipo_retorno = tipo_retorno
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Const_Tipo_Retorno_Expr(self)
    
class Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, tipo_retorno, expr, decl_interna):
        self.tipo_retorno = tipo_retorno
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(self)


class Decl_Interna_Const_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Const_Expr_Decl_Interna(self)


class Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, tipo_retorno, expr, decl_interna):
        self.tipo_retorno = tipo_retorno
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(self)
    
class Decl_Interna_Equal_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Equal_Expr(self)


class Decl_Interna_PlusEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusEqual_Expr(self)


class Decl_Interna_PlusPercent_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPercent_Expr(self)


class Decl_Interna_PlusPercentEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPercentEqual_Expr(self)


class Decl_Interna_PlusPipe_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPipe_Expr(self)
    


class Decl_Interna_Equal_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Equal_Expr_Decl_Interna(self)


class Decl_Interna_PlusEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusEqual_Expr_Decl_Interna(self)


class Decl_Interna_PlusPercent_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPercent_Expr_Decl_Interna(self)


class Decl_Interna_PlusPercentEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPercentEqual_Expr_Decl_Interna(self)


class Decl_Interna_PlusPipe_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPipe_Expr_Decl_Interna(self)
    
    
class Decl_Interna_PlusPipeEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPipeEqual_Expr(self)


class Decl_Interna_MinusEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusEqual_Expr(self)


class Decl_Interna_MinusPercent_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPercent_Expr(self)


class Decl_Interna_MinusPercentEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPercentEqual_Expr(self)


class Decl_Interna_MinusPipe_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPipe_Expr(self)


class Decl_Interna_MinusPipeEqual_Expr(Decl_InternaAbstract):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPipeEqual_Expr(self)
    
    
class Decl_Interna_PlusPipeEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_PlusPipeEqual_Expr_Decl_Interna(self)


class Decl_Interna_MinusEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusEqual_Expr_Decl_Interna(self)


class Decl_Interna_MinusPercent_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPercent_Expr_Decl_Interna(self)


class Decl_Interna_MinusPercentEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPercentEqual_Expr_Decl_Interna(self)


class Decl_Interna_MinusPipe_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPipe_Expr_Decl_Interna(self)


class Decl_Interna_MinusPipeEqual_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_MinusPipeEqual_Expr_Decl_Interna(self)
    
class Decl_Interna_Expr_Decl_Interna(DeclAbstract):

    def __init__(self, expr,decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl__Interna_Expr_Decl_Interna(self) 


class Decl_Interna_Break_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, decl_interna):
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Break_Decl_Interna(self)


class Decl_Interna_Return_Expr_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna):
        self.expr = expr
        self.decl_interna = decl_interna

    def accept(self, visitor):
        return visitor.visitDecl_Interna_Return_Expr_Decl_Interna(self)


class Decl_Interna_While_Expr_Decl_Interna_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna1, decl_interna2):
        self.expr = expr
        self.decl_interna1 = decl_interna1
        self.decl_interna2 = decl_interna2

    def accept(self, visitor):
        return visitor.visitDecl_Interna_While_Expr_Decl_Interna_Decl_Interna(self)


class Decl_Interna_For_Decl_Interna_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, decl_interna1, decl_interna2):
        self.decl_interna1 = decl_interna1
        self.decl_interna2 = decl_interna2

    def accept(self, visitor):
        return visitor.visitDecl_Interna_For_Decl_Interna_Decl_Interna(self)


class Decl_Interna_If_Expr_Decl_Interna_Decl_Interna(Decl_InternaAbstract):

    def __init__(self, expr, decl_interna1, decl_interna2):
        self.expr = expr
        self.decl_interna1 = decl_interna1
        self.decl_interna2 = decl_interna2

    def accept(self, visitor):
        return visitor.visitDecl_Interna_If_Expr_Decl_Interna_Decl_Interna(self)