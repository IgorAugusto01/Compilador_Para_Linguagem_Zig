# AssemblyST.py

# ============================================================
# TABELA DE SÍMBOLOS PARA GERAÇÃO DE ASSEMBLY
# ============================================================

symbolTable = []


# ============================================================
# ATRIBUTOS
# ============================================================

BINDABLE = 'bindable'
TYPE = 'type'
OFFSET = 'offset'
PARAMS = 'params'
SCOPE = 'scope'


# ============================================================
# CATEGORIAS
# ============================================================

VARIABLE = 'var'
CONSTANT = 'const'
FUNCTION = 'fn'


# ============================================================
# TIPOS
# ============================================================

I8 = 'i8'
U8 = 'u8'

I16 = 'i16'
U16 = 'u16'

I32 = 'i32'
U32 = 'u32'

I64 = 'i64'
U64 = 'u64'

I128 = 'i128'
U128 = 'u128'

BOOL = 'bool'
VOID = 'void'


# ============================================================
# ESCOPOS
# ============================================================

SCOPE_MAIN = 'main'


# ============================================================
# CONTROLE DA PILHA
# ============================================================

sp = 0


def getSP():
    return sp


def addSP(value):
    global sp
    sp += value


# ============================================================
# ESCOPOS
# ============================================================

def beginScope(nameScope):

    global symbolTable

    symbolTable.append({
        SCOPE: nameScope
    })


def endScope():

    global symbolTable

    if len(symbolTable) > 0:
        symbolTable.pop()


def getScope():

    global symbolTable

    if len(symbolTable) == 0:
        return None

    return symbolTable[-1][SCOPE]


# ============================================================
# VARIÁVEIS
# ============================================================

def addVar(name, type):

    global symbolTable

    # Cada variável ocupa 4 bytes.
    addSP(-4)

    symbolTable[-1][name] = {
        BINDABLE: VARIABLE,
        TYPE: type,
        OFFSET: getSP()
    }


# ============================================================
# CONSTANTES
# ============================================================

def addConst(name, type):

    global symbolTable

    addSP(-4)

    symbolTable[-1][name] = {
        BINDABLE: CONSTANT,
        TYPE: type,
        OFFSET: getSP()
    }


# ============================================================
# FUNÇÕES
# ============================================================

def addFunction(name, params, returnType):

    global symbolTable

    symbolTable[-1][name] = {
        BINDABLE: FUNCTION,
        PARAMS: params,
        TYPE: returnType
    }


# ============================================================
# BUSCA DE IDENTIFICADOR
# ============================================================

def getBindable(bindableName):

    global symbolTable

    for i in reversed(range(len(symbolTable))):

        if bindableName in symbolTable[i]:

            return symbolTable[i][bindableName]

    return None


# ============================================================
# BUSCA DE ESCOPO
# ============================================================

def getScopeOf(bindableName):

    global symbolTable

    for i in reversed(range(len(symbolTable))):

        if bindableName in symbolTable[i]:

            return symbolTable[i][SCOPE]

    return None