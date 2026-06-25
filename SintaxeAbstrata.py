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