
from abc import ABCMeta,  abstractmethod




class AbstractVisitor(metaclass = ABCMeta):
    
    @abstractmethod   
    def visitPrograma_Funcao(self,Programa_Funcao): pass
    
    @abstractmethod
    def visitPrograma_Decl(self,Program_Decl): pass

    @abstractmethod
    def visitPrograma_Funcao_Programa(self,Programa_Funcao_Programa): pass
    
    @abstractmethod
    def visitFuncao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(self,Funcao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna) : pass
    
    
    
    
    
    
    
    

    
    