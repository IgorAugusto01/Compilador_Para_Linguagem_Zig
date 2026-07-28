from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *



def blank():
    p = ''
    p = p + ' '
    return p

class Visitor(AbstractVisitor):
    
    def visitPrograma_Funcao(self, Programa_Funcao):
        Programa_Funcao.funcao.accept(self)
        
    def visitPrograma_Decl(self, Programa_Decl):
        Programa_Decl.Programa_Decl.decl.accept(self)
    
    def visitPrograma_Funcao_Programa(self, Programa_Funcao_Programa):
       Programa_Funcao_Programa.funcao.accept(self)
       Programa_Funcao_Programa.programa.accept(self)
    
    def visitPrograma_Decl_Programa(self, Programa_Decl_Programa):
        Programa_Decl_Programa.Programa_Decl_Programa.decl.accept(self)
        Programa_Decl_Programa.Programa_Decl_Programa.programa.accept(self)
    
    def visitFuncao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(self, Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna):
        print('pub fn',end='')
        print(Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna.id,end='')
        print('(',end='')
        Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna.params.accept(self)
        print(')',end='')
        Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna.tipo_retorno.accept(self)
        print('{',end='')
        Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna.decl_interna.accept(self)
        print('}')
        
    def visitFuncao_Pub_Fn_Tipo_Retorno_Decl_Interna(self, Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna):
        print('pub fn',end='')
        print(Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna.id,end='')
        print('(',end='')
        print(')',end='')
        Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna.tipo_retorno.accept(self)
        print('{',end='')
        Funcao_Pub_Fn_Tipo_Retorno_Decl_Interna.decl_interna.accept(self)
        print('}')
        
    def visitFuncao_Fn_Params_Tipo_Retorno_Decl_Interna(self, Funcao_Fn_Params_Tipo_Retorno_Decl_Interna):
        print('fn',end='')
        print( Funcao_Fn_Params_Tipo_Retorno_Decl_Interna.id,end='')
        print('(',end='')
        Funcao_Fn_Params_Tipo_Retorno_Decl_Interna.params.accept(self)
        print(')',end='')
        Funcao_Fn_Params_Tipo_Retorno_Decl_Interna.tipo_retorno.accept(self)
        print('{',end='')
        Funcao_Fn_Params_Tipo_Retorno_Decl_Interna.decl_interna.accept(self)
        print('}')
    
    def visitFuncao_Fn_Tipo_Retorno_Decl_Interna(self, Funcao_Fn_Tipo_Retorno_Decl_Interna):
            print('fn',end='')
            print(Funcao_Fn_Tipo_Retorno_Decl_Interna.id,end='')
            print('(',end='')
            print(')',end='')
            Funcao_Fn_Tipo_Retorno_Decl_Interna.tipo_retorno.accept(self)
            print('{',end='')
            Funcao_Fn_Tipo_Retorno_Decl_Interna.decl_interna.accept(self)
            print('}')
    
    
    def visitFuncao_Pub_Fn_Params_Tipo_Retorno(self, Funcao_Pub_Fn_Params_Tipo_Retorno):
        print('pub fn',end='')
        print(Funcao_Pub_Fn_Params_Tipo_Retorno.id,end='')
        print('(',end='')
        Funcao_Pub_Fn_Params_Tipo_Retorno.params.accept(self)
        print(')',end='')
        Funcao_Pub_Fn_Params_Tipo_Retorno.tipo_retorno.accept(self)
        print('{',end='')
        print('}')
        
        
        
    def visitFuncao_Fn_Params_Tipo_Retorno(self, Funcao_Fn_Params_Tipo_Retorno):
            print('fn',end='')
            print(Funcao_Fn_Params_Tipo_Retorno.id,end='')
            print('(',end='')
            Funcao_Fn_Params_Tipo_Retorno.params.accept(self)
            print(')',end='')
            Funcao_Fn_Params_Tipo_Retorno.tipo_retorno.accept(self)
            print('{',end='')
            print('}')
     
     
    def visitFuncao_Pub_Fn_Tipo_Retorno(self, Funcao_Pub_Fn_Tipo_Retorno):
            print('pub fn',end='')
            print(Funcao_Pub_Fn_Tipo_Retorno.id,end='')
            print('(',end='')
            print(')',end='')
            Funcao_Pub_Fn_Tipo_Retorno.tipo_retorno.accept(self)
            print('{',end='')
            print('}')  
            
    def visitFuncao_Fn_Tipo_Retorno(self, Funcao_Fn_Tipo_Retorno):
                print('fn',end='')
                print(Funcao_Fn_Tipo_Retorno.id,end='')
                print('(',end='')
                print(')',end='')
                Funcao_Fn_Tipo_Retorno.tipo_retorno.accept(self)
                print('{',end='')
                print('}')  

    def visitTipo_Retorno(self, Tipo_Retorno):
        Tipo_Retorno.tipo.accept(self)
        
    def visitParams_Id_Tipo_Retorno(self, Params_Id_Tipo_Retorno):
        print(Params_Id_Tipo_Retorno.id,end='')
        print(',',end='')
        Params_Id_Tipo_Retorno.tipo_retorno.accept(self)
        
        
    def visitParams_Id_Tipo_Retorno_Params(self, Params_Id_Tipo_Retorno_Params):
        print(Params_Id_Tipo_Retorno_Params.id,end='')
        print(',',end='')
        Params_Id_Tipo_Retorno_Params.tipo_retorno.accept(self)
        print(',',end='')
        Params_Id_Tipo_Retorno_Params.params.accept(self)
        
    def visitCall_Args(self, Call_Args):
        print(Call_Args.id,end='')
        print('(',end='')
        Call_Args.args.accept(self)
        print(')',end='')
        
    def visitCall_No_Args(self, Call_No_Args):
        print(Call_No_Args.id,end='')
        print('(',end='')
        print(')',end='')
    
    def visitArgs_Id(self, Args_Id):
        print(Args_Id.id,end='')
        
    def visitArgs_Id_Args(self, Args_Id_Args):
        print(Args_Id_Args.id,end='')
        print(',',end='')
        Args_Id_Args.args.accept(self)
    
    def visitArgs_String_Args(self, Args_String_Args):
        print(Args_String_Args.string,end='')
        print(',',end='')            
        print('.',end='')   
        print('{',end='')   
        Args_String_Args.args.accept(self)
        print('}',end='')   
        
    def visitArgs_String(self, Args_String):
            print(Args_String.string,end='')
            print(',',end='')            
            print('.',end='')   
            print('{',end='')   
            print('}',end='') 
    
    def visitDecl_Var_Tipo_Retorno_Expr(self, Decl_Var_Tipo_Retorno_Expr):
        print('var',end='')
        print(Decl_Var_Tipo_Retorno_Expr.id,end='')
        print(',',end='')
        Decl_Var_Tipo_Retorno_Expr.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Var_Tipo_Retorno_Expr.expr.accept(self)
        print(';',end='')
        
    def visitDecl_Const_Expr(self,Decl_Const_Expr):
       print('const',end='')
       print(Decl_Const_Expr.id,end='')
       print('=',end='')
       Decl_Const_Expr.expr.accept(self)
       print(';',end='')
       
       
    def visitDecl_Const_Tipo_Retorno_Expr(self,Decl_Const_Tipo_Retorno_Expr):
        print('const',end='')
        print(Decl_Const_Tipo_Retorno_Expr.id,end='')
        print(':',end='')
        Decl_Const_Tipo_Retorno_Expr.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Const_Tipo_Retorno_Expr.expr.accept(self)
        print(';',end='')
        
    def visitDecl_Equal_Expr(self,Decl_Equal_Expr):
        print(Decl_Equal_Expr.id,end='')
        print('=',end='')
        Decl_Equal_Expr.expr.accept(self)
        print(';',end='')
        
    def visitDecl_Expr(self,Decl_Expr):
        Decl_Expr.expr.accept(self)
        print(';',end='')
       
    def visitDecl_Id_PlusEqual_Expr(self,Decl_Id_PlusEqual_Expr):
        print(Decl_Id_PlusEqual_Expr.id,end='')
        print('+=',end='')
        Decl_Id_PlusEqual_Expr.expr.accept(self)
        print(';',end='')   
        
    def visitDecl_Id_PlusPercent_Expr(self,Decl_Id_PlusPercent_Expr):
        print(Decl_Id_PlusPercent_Expr.id,end='')
        print('+%',end='')
        Decl_Id_PlusPercent_Expr.expr.accept(self)
        print(';',end='')   
        
        
    def visitDecl_Id_PlusPercentEqual_Expr(self,Decl_Id_PlusPercentEqual_Expr):
        print(Decl_Id_PlusPercentEqual_Expr.id,end='')
        print('+%=',end='')
        Decl_Id_PlusPercentEqual_Expr.expr.accept(self)
        print(';',end='')            
        
    def visitDecl_Id_PlusPipe_Expr(self,Decl_Id_PlusPipe_Expr):
        print(Decl_Id_PlusPipe_Expr.id,end='')
        print('+|',end='')
        Decl_Id_PlusPipe_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Id_PlusPipeEqual_Expr(self,Decl_Id_PlusPipeEqual_Expr):
        print(Decl_Id_PlusPipeEqual_Expr.id,end='')
        print('+|=',end='')
        Decl_Id_PlusPipeEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Id_MinusEqual_Expr(self,Decl_Id_MinusEqual_Expr):
        print(Decl_Id_MinusEqual_Expr.id,end='')
        print('-=',end='')
        Decl_Id_MinusEqual_Expr.expr.accept(self)
        print(';',end='')    
        
        
    def visitDecl_Id_MinusPercent_Expr(self,Decl_Id_MinusPercent_Expr):
        print(Decl_Id_MinusPercent_Expr.id,end='')
        print('-%',end='')
        Decl_Id_MinusPercent_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Id_MinusPercentEqual_Expr(self,Decl_Id_MinusPercentEqual_Expr):
        print(Decl_Id_MinusPercentEqual_Expr.id,end='')
        print('-%=',end='')
        Decl_Id_MinusPercentEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Id_MinusPipe_Expr(self,Decl_Id_MinusPipe_Expr):
        print(Decl_Id_MinusPipe_Expr.id,end='')
        print('-|',end='')
        Decl_Id_MinusPipe_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Id_MinusPipeEqual_Expr(self,Decl_Id_MinusPipeEqual_Expr):
        print(Decl_Id_MinusPipeEqual_Expr.id,end='')
        print('-|=',end='')
        Decl_Id_MinusPipeEqual_Expr.expr.accept(self)
        print(';',end='')    
         

    def visitExpr_BuiltinIdentifier_String(self,Expr_BuiltinIdentifier_String):
        Expr_BuiltinIdentifier_String.builtindentifier.accept(self)
        print('(',end='')
        Expr_BuiltinIdentifier_String.string.accept(self)
        print(')',end='')


    def visitExpr_BuiltinIdentifier_Expr(self,Expr_BuiltinIdentifier_Expr):
        Expr_BuiltinIdentifier_Expr.builtindentifier.accept(self)
        print('(',end='')
        Expr_BuiltinIdentifier_Expr.expr1.accept(self)
        print(')',end='')
        print('.',end='')
        Expr_BuiltinIdentifier_Expr.expr2.accept(self)

    def visitExpr_Id_Plus_Expr(self,Expr_Id_Plus_Expr):
        print(Expr_Id_Plus_Expr.id,end='')
        print('+',end='')
        Expr_Id_Plus_Expr.expr.accept(self)


    def visitExpr_Id(self,Expr_Id):
        Expr_Id.id.accept(self)


    def visitExpr_Id_Expr(self,Expr_Id_Expr):
        Expr_Id_Expr.id.accept(self)
        print('.',end='')
        Expr_Id_Expr.expr.accept(self)

    def visitExpr_Call(self,Expr_Call):
        Expr_Call.call.accept(self)


    def visitExpr_Integer(self,Expr_Integer):
        print(Expr_Integer.integer,end='')


    def visitExpr_Id_Minus_Expr(self,Expr_Id_Minus_Expr):
        Expr_Id_Minus_Expr.id.accept(self)
        print('-',end='')
        Expr_Id_Minus_Expr.expr.accept(self)


    def visitExpr_Id_Slash_Expr(self,Expr_Id_Slash_Expr):
        Expr_Id_Slash_Expr.id.accept(self)
        print('/',end='')
        Expr_Id_Slash_Expr.expr.accept(self)


    def visitExpr_Id_Asterisk_Expr(self,Expr_Id_Asterisk_Expr):
        Expr_Id_Asterisk_Expr.id.accept(self)
        print('*',end='')
        Expr_Id_Asterisk_Expr.expr.accept(self)


    def visitExpr_Id_Rarrow_Expr(self,Expr_Id_Rarrow_Expr):
        Expr_Id_Rarrow_Expr.id.accept(self)
        print('>',end='')
        Expr_Id_Rarrow_Expr.expr.accept(self)


    def visitExpr_Id_Larrow_Expr(self,Expr_Id_Larrow_Expr):
        Expr_Id_Larrow_Expr.id.accept(self)
        print('<',end='')
        Expr_Id_Larrow_Expr.expr.accept(self)


    def visitExpr_Id_Percent_Expr(self,Expr_Id_Percent_Expr):
        Expr_Id_Percent_Expr.id.accept(self)
        print('%',end='')
        Expr_Id_Percent_Expr.expr.accept(self)
        
        
        
        
    def visitExpr_Id_EqualEqual_Expr(self,Expr_Id_EqualEqual_Expr):
        Expr_Id_EqualEqual_Expr.id.accept(self)
        print('==',end='')
        Expr_Id_EqualEqual_Expr.expr.accept(self)


    def visitExpr_Id_And_Expr(self,Expr_Id_And_Expr):
        Expr_Id_And_Expr.id.accept(self)
        print('and',end='')
        Expr_Id_And_Expr.expr.accept(self)


    def visitExpr_Id_Or_Expr(self,Expr_Id_Or_Expr):
        Expr_Id_Or_Expr.id.accept(self)
        print('or',end='')
        Expr_Id_Or_Expr.expr.accept(self)


    def visitExpr_True(self,Expr_True):
        print(Expr_True.true,end='')


    def visitExpr_False(self,Expr_False):
        print(Expr_False.false,end='')   
        
    def visitDecl_Interna_Break(self,Decl_Interna_Break):
        print(Decl_Interna_Break.break_tok,end='')
        print(';',end='')

    def visitDecl_Interna_Expr(self, Decl_Interna_Expr):
        Decl_Interna_Expr.expr.accept(self)
        print(';',end='')
        
    def visitParams_Id_Tipo_Retorno(self,Params_Id_Tipo_Retorno):
        Params_Id_Tipo_Retorno.id.accept(self)
        print(':',end='')
        Params_Id_Tipo_Retorno.tipo_retorno.accept(self)


    def visitParams_Id_Tipo_Retorno_Params(self,Params_Id_Tipo_Retorno_Params):
        Params_Id_Tipo_Retorno_Params.id.accept(self)
        print(':',end='')
        Params_Id_Tipo_Retorno_Params.tipo_retorno.accept(self)
        print(',',end='')
        Params_Id_Tipo_Retorno_Params.params.accept(self)

    def visitDecl_Interna_Return_Expr(self,Decl_Interna_Return_Expr):
        print(Decl_Interna_Return_Expr.return_tok,end='')
        Decl_Interna_Return_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_While_Expr_Decl_Interna(self,Decl_Interna_While_Expr_Decl_Interna):
        print('while',end='')
        print('(',end='')
        Decl_Interna_While_Expr_Decl_Interna.expr.accept(self)
        print(')',end='')
        print('{',end='')
        Decl_Interna_While_Expr_Decl_Interna.decl_interna.accept(self)
        print('}',end='')
        
    def visitDecl_Interna_If_Expr_Decl_Interna(self,Decl_Interna_If_Expr_Decl_Interna):
        print('if',end='')
        print('(',end='')
        Decl_Interna_If_Expr_Decl_Interna.expr.accept(self)
        print(')',end='')
        print('{',end='')
        Decl_Interna_If_Expr_Decl_Interna.decl_interna.accept(self)
        print('}',end='')


    def visitDecl_Interna_Var_Tipo_Retorno_Expr(self,Decl_Interna_Var_Tipo_Retorno_Expr):
        print('var',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr.id.accept(self)
        print(':',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr.expr.accept(self)
        print(';',end='')
        
        
    def visitDecl_Interna_Const_Expr(self,Decl_Interna_Const_Expr):
        print('const',end='')
        Decl_Interna_Const_Expr.id.accept(self)
        print('=',end='')
        Decl_Interna_Const_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_Const_Tipo_Retorno_Expr(self,Decl_Interna_Const_Tipo_Retorno_Expr):
        print('const',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr.id.accept(self)
        print(':',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(self,Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna):
        print('var',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna.id.accept(self)
        print(':',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_Const_Expr_Decl_Interna(self,Decl_Interna_Const_Expr_Decl_Interna):
        print('const',end='')
        Decl_Interna_Const_Expr_Decl_Interna.id.accept(self)
        print('=',end='')
        Decl_Interna_Const_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Const_Expr_Decl_Interna.decl_interna.accept(self)     
        
    
    def visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(self,Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna):
        print('const',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna.id.accept(self)
        print(':',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna.tipo_retorno.accept(self)
        print('=',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_Equal_Expr(self,Decl_Interna_Equal_Expr):
        Decl_Interna_Equal_Expr.id.accept(self)
        print('=',end='')
        Decl_Interna_Equal_Expr.expr.accept(self)
        print(';',end='')
        

    def visitDecl_Interna_PlusEqual_Expr(self,Decl_Interna_PlusEqual_Expr):
        Decl_Interna_PlusEqual_Expr.id.accept(self)
        print('+=',end='')
        Decl_Interna_PlusEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_PlusPercent_Expr(self,Decl_Interna_PlusPercent_Expr):
        Decl_Interna_PlusPercent_Expr.id.accept(self)
        print('+%',end='')
        Decl_Interna_PlusPercent_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_PlusPercentEqual_Expr(self,Decl_Interna_PlusPercentEqual_Expr):
        Decl_Interna_PlusPercentEqual_Expr.id.accept(self)
        print('+%=',end='')
        Decl_Interna_PlusPercentEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_PlusPipe_Expr(self,Decl_Interna_PlusPipe_Expr):
        Decl_Interna_PlusPipe_Expr.id.accept(self)
        print('+|',end='')
        Decl_Interna_PlusPipe_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_Equal_Expr_Decl_Interna(self,Decl_Interna_Equal_Expr_Decl_Interna):
        Decl_Interna_Equal_Expr_Decl_Interna.id.accept(self)
        print('=',end='')
        Decl_Interna_Equal_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Equal_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_PlusEqual_Expr_Decl_Interna(self,Decl_Interna_PlusEqual_Expr_Decl_Interna):
        Decl_Interna_PlusEqual_Expr_Decl_Interna.id.accept(self)
        print('+=',end='')
        Decl_Interna_PlusEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_PlusEqual_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_PlusPercent_Expr_Decl_Interna(self,Decl_Interna_PlusPercent_Expr_Decl_Interna):
        Decl_Interna_PlusPercent_Expr_Decl_Interna.id.accept(self)
        print('+%',end='')
        Decl_Interna_PlusPercent_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_PlusPercent_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_PlusPercentEqual_Expr_Decl_Interna(self,Decl_Interna_PlusPercentEqual_Expr_Decl_Interna):
        Decl_Interna_PlusPercentEqual_Expr_Decl_Interna.id.accept(self)
        print('+%=',end='')
        Decl_Interna_PlusPercentEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_PlusPercentEqual_Expr_Decl_Interna.decl_interna.accept(self)



    def visitDecl_Interna_PlusPipe_Expr_Decl_Interna(self,Decl_Interna_PlusPipe_Expr_Decl_Interna):
        Decl_Interna_PlusPipe_Expr_Decl_Interna.id.accept(self)
        print('+|',end='')
        Decl_Interna_PlusPipe_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_PlusPipe_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_PlusPipeEqual_Expr(self,Decl_Interna_PlusPipeEqual_Expr):
        Decl_Interna_PlusPipeEqual_Expr.id.accept(self)
        print('+|=',end='')
        Decl_Interna_PlusPipeEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_MinusEqual_Expr(self,Decl_Interna_MinusEqual_Expr):
        Decl_Interna_MinusEqual_Expr.id.accept(self)
        print('-=',end='')
        Decl_Interna_MinusEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_MinusPercent_Expr(self,Decl_Interna_MinusPercent_Expr):
        Decl_Interna_MinusPercent_Expr.id.accept(self)
        print('-%',end='')
        Decl_Interna_MinusPercent_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_MinusPercentEqual_Expr(self,Decl_Interna_MinusPercentEqual_Expr):
        Decl_Interna_MinusPercentEqual_Expr.id.accept(self)
        print('-%=',end='')
        Decl_Interna_MinusPercentEqual_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_MinusPipe_Expr(self,Decl_Interna_MinusPipe_Expr):
        Decl_Interna_MinusPipe_Expr.id.accept(self)
        print('-|',end='')
        Decl_Interna_MinusPipe_Expr.expr.accept(self)
        print(';',end='')


    def visitDecl_Interna_MinusPipeEqual_Expr(self,Decl_Interna_MinusPipeEqual_Expr):
        Decl_Interna_MinusPipeEqual_Expr.id.accept(self)
        print('-|=',end='')
        Decl_Interna_MinusPipeEqual_Expr.expr.accept(self)
        print(';',end='')



    def visitDecl_Interna_PlusPipeEqual_Expr_Decl_Interna(self,Decl_Interna_PlusPipeEqual_Expr_Decl_Interna):
        Decl_Interna_PlusPipeEqual_Expr_Decl_Interna.id.accept(self)
        print('+|=',end='')
        Decl_Interna_PlusPipeEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_PlusPipeEqual_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_MinusEqual_Expr_Decl_Interna(self,Decl_Interna_MinusEqual_Expr_Decl_Interna):
        Decl_Interna_MinusEqual_Expr_Decl_Interna.id.accept(self)
        print('-=',end='')
        Decl_Interna_MinusEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_MinusEqual_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_MinusPercent_Expr_Decl_Interna(self,Decl_Interna_MinusPercent_Expr_Decl_Interna):
        Decl_Interna_MinusPercent_Expr_Decl_Interna.id.accept(self)
        print('-%',end='')
        Decl_Interna_MinusPercent_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_MinusPercent_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_MinusPercentEqual_Expr_Decl_Interna(self,Decl_Interna_MinusPercentEqual_Expr_Decl_Interna):
        Decl_Interna_MinusPercentEqual_Expr_Decl_Interna.id.accept(self)
        print('-%=',end='')
        Decl_Interna_MinusPercentEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_MinusPercentEqual_Expr_Decl_Interna.decl_interna.accept(self)

    def visitDecl_Interna_MinusPipe_Expr_Decl_Interna(self,Decl_Interna_MinusPipe_Expr_Decl_Interna):
        Decl_Interna_MinusPipe_Expr_Decl_Interna.id.accept(self)
        print('-|',end='')
        Decl_Interna_MinusPipe_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_MinusPipe_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_MinusPipeEqual_Expr_Decl_Interna(self,Decl_Interna_MinusPipeEqual_Expr_Decl_Interna):
        Decl_Interna_MinusPipeEqual_Expr_Decl_Interna.id.accept(self)
        print('-|=',end='')
        Decl_Interna_MinusPipeEqual_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_MinusPipeEqual_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl__Interna_Expr_Decl_Interna(self,Decl_Interna_Expr_Decl_Interna):
        Decl_Interna_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Expr_Decl_Interna.decl_interna.accept(self)

    def visitDecl_Interna_Break_Decl_Interna(self,Decl_Interna_Break_Decl_Interna):
        print(Decl_Interna_Break_Decl_Interna.break_tok,end='')
        print(';',end='')
        Decl_Interna_Break_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_Return_Expr_Decl_Interna(self,Decl_Interna_Return_Expr_Decl_Interna):
        print(Decl_Interna_Return_Expr_Decl_Interna.return_tok,end='')
        Decl_Interna_Return_Expr_Decl_Interna.expr.accept(self)
        print(';',end='')
        Decl_Interna_Return_Expr_Decl_Interna.decl_interna.accept(self)


    def visitDecl_Interna_While_Expr_Decl_Interna_Decl_Interna(self,Decl_Interna_While_Expr_Decl_Interna_Decl_Interna):
        print('while',end='')
        print('(',end='')
        Decl_Interna_While_Expr_Decl_Interna_Decl_Interna.expr.accept(self)
        print(')',end='')
        print('{',end='')
        Decl_Interna_While_Expr_Decl_Interna_Decl_Interna.decl_interna1.accept(self)
        print('}',end='')
        Decl_Interna_While_Expr_Decl_Interna_Decl_Interna.decl_interna2.accept(self)


    def visitDecl_Interna_For_Decl_Interna_Decl_Interna(self,Decl_Interna_For_Decl_Interna_Decl_Interna):
        print('for',end='')
        print('(',end='')
        print(Decl_Interna_For_Decl_Interna_Decl_Interna.integer1,end='')
        print('..',end='')
        print(Decl_Interna_For_Decl_Interna_Decl_Interna.integer2,end='')
        print(')',end='')
        print('|',end='')
        Decl_Interna_For_Decl_Interna_Decl_Interna.id.accept(self)
        print('|',end='')
        print('{',end='')
        Decl_Interna_For_Decl_Interna_Decl_Interna.decl_interna1.accept(self)
        print('}',end='')
        Decl_Interna_For_Decl_Interna_Decl_Interna.decl_interna2.accept(self)
    
    def visitDecl_Interna_For_Decl_Interna(self,Decl_Interna_For_Decl_Interna):
        print('for',end='')
        print('(',end='')
        print(Decl_Interna_For_Decl_Interna.integer1,end='')
        print('..',end='')
        print(Decl_Interna_For_Decl_Interna.integer2,end='')
        print(')',end='')
        print('|',end='')
        Decl_Interna_For_Decl_Interna.id.accept(self)
        print('|',end='')
        print('{',end='')
        Decl_Interna_For_Decl_Interna.decl_interna.accept(self)
        print('}',end='')
        


    def visitDecl_Interna_If_Expr_Decl_Interna_Decl_Interna(self,Decl_Interna_If_Expr_Decl_Interna_Decl_Interna):
        print('if',end='')
        print('(',end='')
        Decl_Interna_If_Expr_Decl_Interna_Decl_Interna.expr.accept(self)
        print(')',end='')
        print('{',end='')
        Decl_Interna_If_Expr_Decl_Interna_Decl_Interna.decl_interna1.accept(self)
        print('}',end='')
        Decl_Interna_If_Expr_Decl_Interna_Decl_Interna.decl_interna2.accept(self)







def main():
    f = open("ex/exemplo.zig", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc(debug=True)
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

if __name__ == "__main__":
    main()