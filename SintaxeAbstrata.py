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




###################### DEFINIÇÃO DA CLASSE ABSTRATA TIPO_RETORNO  #########################


class Tipo_RetornoAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass

class Tipo_Retorno_Void(Tipo_RetornoAbstract):
    def __init__(self, void):
        self.void = void

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_Void(self)



class Tipo_Retorno_I8(Tipo_RetornoAbstract):
    def __init__(self, i8):
        self.i8 = i8

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I8(self)



class Tipo_Retorno_U8(Tipo_RetornoAbstract):
    def __init__(self, u8):
        self.u8 = u8

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_U8(self)



class Tipo_Retorno_I16(Tipo_RetornoAbstract):
    def __init__(self, i16):
        self.i16 = i16

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)



class Tipo_Retorno_U16(Tipo_RetornoAbstract):
    def __init__(self, u16):
        self.u16 = u16

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)



class Tipo_Retorno_I32(Tipo_RetornoAbstract):
    def __init__(self, i32):
        self.i32 = i32

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)



class Tipo_Retorno_U32(Tipo_RetornoAbstract):
    def __init__(self, u32):
        self.u32 = u32

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)




class Tipo_Retorno_I64(Tipo_RetornoAbstract):
    def __init__(self, i64):
        self.i64 = i64

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)




class Tipo_Retorno_I128(Tipo_RetornoAbstract):
    def __init__(self, i128):
        self.i128 = i128

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)




class Tipo_Retorno_U128(Tipo_RetornoAbstract):
    def __init__(self, u128):
        self.u128 = u128

    def accept(self, visitor):
        return visitor.visitTipo_Retorno_I16(self)






###################### DEFINIÇÃO DA CLASSE ABSTRATA PARAMS  #########################


class ParamsAbstract(ABC):
      @abstractmethod
    def accept(self, visitor):
        pass

class Params_ID_Tipo_Retorno(ParamsAbstract):

    def __init__(self,ID,tipo_retorno):
        self.ID = ID
        self.tipo_retorno = tipo_retorno

    def accept(self, visitor):
        return visitor.visitParams_ID_Tipo_Retorno(self)




class Params_ID_Tipo_Retorno_Params(ParamsAbstract):

    def __init__(self,ID,tipo_retorno,params):
        self.ID = ID
        self.tipo_retorno = tipo_retorno
        self.params = params

    def accept(self, visitor):
        return visitor.visitParams_ID_Tipo_Retorno_Params(self)


###################### DEFINIÇÃO DA CLASSE ABSTRATA CORPO  #########################




class CorpoAbstract(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Corpo_Comandos(CorpoAbstract):

    def __init__(self,comandos):
        self.comandos = comandos

     def accept(self, visitor):
        return visitor.visitCorpo_Comandos(self)
    
    
    
