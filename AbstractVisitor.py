
from abc import ABCMeta,  abstractmethod




class AbstractVisitor(metaclass = ABCMeta):
    
    @abstractmethod   
    def visitPrograma_Funcao(self,Programa_Funcao): pass
    
    @abstractmethod
    def visitPrograma_Decl(self,Program_Decl): pass

    @abstractmethod
    def visitPrograma_Funcao_Programa(self,Programa_Funcao_Programa): pass
    
    @abstractmethod
    def visitPrograma_Decl_Programa(self,Programa_Decl_Programa): pass
    
    @abstractmethod
    def visitFuncao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(self,Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna):pass
    
    @abstractmethod
    def visitFuncao_Pub_Fn_Tipo_Retorno_Decl_Interna(self,Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna):pass
    
    @abstractmethod
    def visitFuncao_Fn_Params_Tipo_Retorno_Decl_Interna(self,Funcao_Fn_Params_Tipo_Retorno_Decl_Interna):pass
    
    @abstractmethod
    def visitFuncao_Fn_Tipo_Retorno_Decl_Interna(self,Funcao_Fn_Tipo_Retorno_Decl_Interna):pass
    
    @abstractmethod
    def visitFuncao_Pub_Fn_Params_Tipo_Retorno(self,Funcao_Pub_Fn_Params_Tipo_Retorno):pass
    
    @abstractmethod
    def visitFuncao_Fn_Params_Tipo_Retorno(self,Funcao_Fn_Params_Tipo_Retorno):pass
    
    @abstractmethod
    def visitFuncao_Pub_Fn_Tipo_Retorno(self,Funcao_Pub_Fn_Tipo_Retorno):pass
        
    @abstractmethod
    def visitFuncao_Fn_Tipo_Retorno(self,Funcao_Fn_Tipo_Retorno):pass
    
    @abstractmethod
    def visitTipo_Retorno(self,Tipo_Retorno):pass
    
    @abstractmethod
    def visitParams_Id_Tipo_Retorno(self,Params_IdTipo_Retorno):pass
    
    @abstractmethod
    def visitParams_Id_Tipo_Retorno_Params(self,Params_IdTipo_Retorno_Params):pass  
    
    @abstractmethod
    def visitCall_Args(self,Call_Args):pass 
    
    @abstractmethod
    def visitCall_No_Args(self,Call_No_Args):pass
    
    @abstractmethod
    def visitArgs_Id(self,Args_Id):pass
    
    @abstractmethod
    def visitArgs_Id_Args(self,Args_Id_Args):pass
    
    @abstractmethod
    def visitArgs_String_Args(self,Args_String_Args):pass
    
    @abstractmethod
    def visitArgs_String(self,Args_String):pass
    
    @abstractmethod
    def visitDecl_Var_Tipo_Retorno_Expr(self,Decl_Var_Tipo_Retorno_Expr):pass
    
    @abstractmethod
    def visitDecl_Const_Expr(self,Decl_Const_Expr):pass
    
    @abstractmethod
    def visitDecl_Const_Tipo_Retorno_Expr(self,Decl_Const_Tipo_Retorno_Expr):pass
    
    @abstractmethod
    def visitDecl_Equal_Expr(self,Decl_Equal_Expr):pass
    
    @abstractmethod
    def visitDecl_Expr(self,Decl_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_PlusEqual_Expr(self,Decl_Id_PlusEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_PlusPercent_Expr(self,Decl_Id_PlusPercent_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_PlusPercentEqual_Expr(self,Decl_Id_PlusPercentEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_PlusPipe_Expr(self,Decl_Id_PlusPipe_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_PlusPipeEqual_Expr(self,Decl_Id_PlusPipeEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_MinusEqual_Expr(self,Decl_Id_MinusEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_MinusPercent_Expr(self,Decl_Id_MinusPercent_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_MinusPercentEqual_Expr(self,Decl_Id_MinusPercentEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_MinusPipe_Expr(self,Decl_Id_MinusPipe_Expr):pass
    
    @abstractmethod
    def visitDecl_Id_MinusPipeEqual_Expr(self,Decl_Id_MinusPipeEqual_Expr):pass
    
    @abstractmethod
    def visitExpr_BuiltinIdentifier_String(self,Expr_BuiltinIdentifier_String):pass
    
    @abstractmethod
    def visitExpr_BuiltinIdentifier_Expr(self,Expr_BuiltinIdentifier_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Plus_Expr(self,Expr_Id_Plus_Expr):pass
    
    @abstractmethod
    def visitExpr_Id(self,Expr_Id):pass
    
    @abstractmethod
    def visitExpr_Id_Expr(self,Expr_Id_Expr):pass
    
    @abstractmethod
    def visitExpr_Call(self,Expr_Call):pass
    
    @abstractmethod
    def visitExpr_Integer(self,Expr_Integer):pass
    
    @abstractmethod
    def visitExpr_Id_Minus_Expr(self,Expr_Id_Minus_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Slash_Expr(self,Expr_Id_Slash_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Asterisk_Expr(self,Expr_Id_Asterisk_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Rarrow_Expr(self,Expr_Id_Rarrow_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Larrow_Expr(self,Expr_Id_Larrow_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Percent_Expr(self,Expr_Id_Percent_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_EqualEqual_Expr(self,Expr_Id_EqualEqual_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_And_Expr(self,Expr_Id_And_Expr):pass
    
    @abstractmethod
    def visitExpr_Id_Or_Expr(self,Expr_Id_Or_Expr):pass
    
    @abstractmethod
    def visitExpr_True(self,Expr_True):pass
    
    @abstractmethod
    def visitExpr_False(self,Expr_False):pass
    
    @abstractmethod
    def visitDecl_Interna_Break(self,Decl_Interna_Break):pass

    @abstractmethod
    def visitDecl_Interna_Return_Expr(self,Decl_Interna_Return_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_While_Expr_Decl_Interna(self,Decl_Interna_While_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_For_Decl_Interna(self,Decl_Interna_For_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_Expr(self,Decl__Interna_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_If_Expr_Decl_Interna(self,Decl_Interna_If_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_Var_Tipo_Retorno_Expr(self,Decl_Interna_Var_Tipo_Retorno_Expr):pass

    @abstractmethod
    def visitDecl_Interna_Const_Expr(self,Decl_Interna_Const_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_Const_Tipo_Retorno_Expr(self,Decl_Interna_Const_Tipo_Retorno_Expr):pass

    @abstractmethod
    def visitDecl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(self,Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_Const_Expr_Decl_Interna(self,Decl_Interna_Const_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(self,Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_Equal_Expr(self,Decl_Interna_Equal_Expr):pass

    @abstractmethod
    def visitDecl_Interna_PlusEqual_Expr(self,Decl_Interna_PlusEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_PlusPercent_Expr(self,Decl_Interna_PlusPercent_Expr):pass

    @abstractmethod
    def visitDecl_Interna_PlusPercentEqual_Expr(self,Decl_Interna_PlusPercentEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_PlusPipe_Expr(self,Decl_Interna_PlusPipe_Expr):pass

    @abstractmethod
    def visitDecl_Interna_Equal_Expr_Decl_Interna(self,Decl_Interna_Equal_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_PlusEqual_Expr_Decl_Interna(self,Decl_Interna_PlusEqual_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_PlusPercent_Expr_Decl_Interna(self,Decl_Interna_PlusPercent_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_PlusPercentEqual_Expr_Decl_Interna(self,Decl_Interna_PlusPercentEqual_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_PlusPipe_Expr_Decl_Interna(self,Decl_Interna_PlusPipe_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_PlusPipeEqual_Expr(self,Decl_Interna_PlusPipeEqual_Expr):pass

    @abstractmethod
    def visitDecl_Interna_MinusEqual_Expr(self,Decl_Interna_MinusEqual_Expr):pass

    @abstractmethod
    def visitDecl_Interna_MinusPercent_Expr(self,Decl_Interna_MinusPercent_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_MinusPercentEqual_Expr(self,Decl_Interna_MinusPercentEqual_Expr):pass

    @abstractmethod
    def visitDecl_Interna_MinusPipe_Expr(self,Decl_Interna_MinusPipe_Expr):pass

    @abstractmethod
    def visitDecl_Interna_MinusPipeEqual_Expr(self,Decl_Interna_MinusPipeEqual_Expr):pass
    
    @abstractmethod
    def visitDecl_Interna_PlusPipeEqual_Expr_Decl_Interna(self,Decl_Interna_PlusPipeEqual_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_MinusEqual_Expr_Decl_Interna(self,Decl_Interna_MinusEqual_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_MinusPercent_Expr_Decl_Interna(self,Decl_Interna_MinusPercent_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_MinusPercentEqual_Expr_Decl_Interna(self,Decl_Interna_MinusPercentEqual_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_MinusPipe_Expr_Decl_Interna(self,Decl_Interna_MinusPipe_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_MinusPipeEqual_Expr_Decl_Interna(self,Decl_Interna_MinusPipeEqual_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl__Interna_Expr_Decl_Interna(self,Decl__Interna_Expr_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_Break_Decl_Interna(self,Decl_Interna_Break_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_Return_Expr_Decl_Interna(self,Decl_Interna_Return_Expr_Decl_Interna):pass
    
    @abstractmethod
    def visitDecl_Interna_While_Expr_Decl_Interna_Decl_Interna(self,Decl_Interna_While_Expr_Decl_Interna_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_For_Decl_Interna_Decl_Interna(self,Decl_Interna_For_Decl_Interna_Decl_Interna):pass

    @abstractmethod
    def visitDecl_Interna_If_Expr_Decl_Interna_Decl_Interna(self,Decl_Interna_If_Expr_Decl_Interna_Decl_Interna):pass