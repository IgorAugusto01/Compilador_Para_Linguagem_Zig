# TabelaSimbolos.py

symbolTable = []

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
# CATEGORIAS
# ============================================================

VARIABLE = 'var'
CONSTANT = 'const'
FUNCTION = 'fn'


# ============================================================
# ATRIBUTOS DA TABELA
# ============================================================

BINDABLE = 'bindable'
TYPE = 'type'
PARAMS = 'params'
SCOPE = 'scope'


# DEBUG = -1 -> imprime a tabela após cada alteração
DEBUG = 0


# ============================================================
# IMPRESSÃO
# ============================================================

def printTable():
    global DEBUG

    if DEBUG == -1:
        print('Tabela:', symbolTable)


# ============================================================
# ESCOPOS
# ============================================================

def beginScope(nameScope):
    global symbolTable

    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

    printTable()


def endScope():
    global symbolTable

    symbolTable = symbolTable[:-1]

    printTable()


# ============================================================
# VARIÁVEIS
# ============================================================

def addVar(name, type):
    global symbolTable

    symbolTable[-1][name] = {
        BINDABLE: VARIABLE,
        TYPE: type
    }

    printTable()


# ============================================================
# CONSTANTES
# ============================================================

def addConst(name, type):
    global symbolTable

    symbolTable[-1][name] = {
        BINDABLE: CONSTANT,
        TYPE: type
    }

    printTable()


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

    printTable()


# ============================================================
# CONSULTA DE IDENTIFICADOR
# ============================================================

def getBindable(bindableName):
    global symbolTable

    for i in reversed(range(len(symbolTable))):
        if bindableName in symbolTable[i]:
            return symbolTable[i][bindableName]

    return None


# ============================================================
# CONSULTA DE ESCOPO
# ============================================================

def getScope(bindableName):
    global symbolTable

    for i in reversed(range(len(symbolTable))):
        if bindableName in symbolTable[i]:
            return symbolTable[i][SCOPE]

    return None


# ============================================================
# TESTE DA TABELA DE SÍMBOLOS
# ============================================================

def main():
    global DEBUG

    DEBUG = -1

    print('\n# Criando escopo main')
    beginScope('main')

    print('\n# Adicionando Vinculavel funcao some')
    addFunction(
        'some',
        ['a', I32, 'b', I32],
        I32
    )

    print('\n# Criando escopo some')
    beginScope('some')

    print('\n# Adicionando var a do tipo i32')
    addVar('a', I32)

    print('\n# Pegar escopo de var a')
    print(getScope('a'))

    print('\n# Adicionando var b do tipo i32')
    addVar('b', I32)

    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))

    print('\n# Consultando bindable')
    print(str(getBindable('some')))

    print('\n# Removendo escopo some')
    endScope()


if __name__ == "__main__":
    main()