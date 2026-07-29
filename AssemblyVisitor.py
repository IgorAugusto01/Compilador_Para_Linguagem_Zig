
from Visitor import Visitor
import ExpressionLanguageParser
from ExpressionLanguageLex import *
import ply.lex as lex
import ply.yacc as yacc


class AssemblyVisitor(Visitor):

    def __init__(self):
        # Código final
        self.code = []

        # Dados do programa
        self.data = []

        # Controle de registradores
        self.temp_registers = [
            "$t0", "$t1", "$t2", "$t3",
            "$t4", "$t5", "$t6", "$t7",
            "$t8", "$t9"
        ]

        self.temp_index = 0

        # Controle de labels
        self.label_count = 0

        # Tabela simples de variáveis:
        # nome -> offset no frame
        self.variables = {}

        self.offset = 0

        # Pilha de contexto para escopos
        self.scope_stack = []

        # Função atual
        self.current_function = None

        # Indica se estamos dentro de main
        self.in_main = False


    # =========================================================
    # UTILITÁRIOS
    # =========================================================

    def emit(self, instruction=""):
        self.code.append(instruction)


    def emit_data(self, instruction):
        self.data.append(instruction)


    def new_label(self, prefix="L"):
        label = f"{prefix}{self.label_count}"
        self.label_count += 1
        return label


    def get_temp(self):
        register = self.temp_registers[
            self.temp_index % len(self.temp_registers)
        ]

        self.temp_index += 1

        return register


    def reset_temps(self):
        self.temp_index = 0


    def get_variable_offset(self, name):

        if name in self.variables:
            return self.variables[name]

        self.offset -= 4
        self.variables[name] = self.offset

        return self.offset


    def load_variable(self, name):

        register = self.get_temp()
        offset = self.get_variable_offset(name)

        self.emit(
            f"lw {register}, {offset}($sp)"
        )

        return register


    def store_variable(self, name, register):

        offset = self.get_variable_offset(name)

        self.emit(
            f"sw {register}, {offset}($sp)"
        )


    def generate(self):

        result = []

        result.append(".data")

        if len(self.data) == 0:
            result.append("")

        else:
            result.extend(self.data)

        result.append("")
        result.append(".text")
        result.append(".globl main")
        result.append("")

        result.extend(self.code)

        return "\n".join(result)


    # =========================================================
    # PROGRAMAS
    # =========================================================

    def visitPrograma_Funcao(self, Programa_Funcao):

        Programa_Funcao.funcao.accept(self)


    def visitPrograma_Decl(self, Programa_Decl):

        Programa_Decl.decl.accept(self)


    def visitPrograma_Decl_Programa(self, Programa_Decl_Programa):

        Programa_Decl_Programa.decl.accept(self)

        Programa_Decl_Programa.programa.accept(self)


    # =========================================================
    # TIPOS
    # =========================================================

    def visitTipo_Retorno(self, node):

        return node.tipo.accept(self)


    def visitTipo(self, node):

        return node.tipo


    # =========================================================
    # FUNÇÕES
    # =========================================================

    def visitFuncao_Pub_Fn_Tipo_Retorno(self, node):

        nome = node.id

        self.current_function = nome
        self.in_main = nome == "main"

        self.variables = {}
        self.offset = 0

        self.emit("")
        self.emit(f"{nome}:")

        self.emit("addi $sp, $sp, -32")
        self.emit("sw $ra, 28($sp)")
        self.emit("sw $fp, 24($sp)")
        self.emit("move $fp, $sp")

        self.scope_stack.append(nome)


    def visitFuncao_Pub_Fn_Tipo_Retorno_Decl_Interna(
        self,
        node
    ):

        nome = node.id

        self.current_function = nome
        self.in_main = nome == "main"

        self.variables = {}
        self.offset = 0

        self.emit("")
        self.emit(f"{nome}:")

        self.emit("addi $sp, $sp, -32")
        self.emit("sw $ra, 28($sp)")
        self.emit("sw $fp, 24($sp)")
        self.emit("move $fp, $sp")

        self.scope_stack.append(nome)

        if node.decl_interna is not None:
            node.decl_interna.accept(self)

        self.emit("")
        self.emit(f"{nome}_end:")

        self.emit("move $sp, $fp")
        self.emit("lw $fp, 24($sp)")
        self.emit("lw $ra, 28($sp)")
        self.emit("addi $sp, $sp, 32")
        self.emit("jr $ra")

        self.scope_stack.pop()


    # =========================================================
    # INTEIROS
    # =========================================================

    def visitExpr_Integer(self, node):

        register = self.get_temp()

        self.emit(
            f"li {register}, {node.integer}"
        )

        return register


    # =========================================================
    # IDENTIFICADOR
    # =========================================================

    def visitExpr_Id(self, node):

        return self.load_variable(node.id)


    # =========================================================
    # SOMA
    # =========================================================

    def visitExpr_Id_Plus_Expr(self, node):

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"add {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # SUBTRAÇÃO
    # =========================================================

    def visitExpr_Expr_Minus_Expr(self, node):

        left = node.expr1.accept(self)

        right = node.expr2.accept(self)

        result = self.get_temp()

        self.emit(
            f"sub {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # MULTIPLICAÇÃO
    # =========================================================

    def visitExpr_Expr_Asterisk_Expr(self, node):

        left = node.expr1.accept(self)

        right = node.expr2.accept(self)

        result = self.get_temp()

        self.emit(
            f"mul {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # DIVISÃO
    # =========================================================

    def visitExpr_Id_Slash_Expr(self, node):

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"div {left}, {right}"
        )

        self.emit(
            f"mflo {result}"
        )

        return result


    # =========================================================
    # COMPARAÇÃO >
    # =========================================================

    def visitExpr_Id_Rarrow_Expr(self, node):

        # node.id é STRING.
        # Portanto, não usamos node.id.accept(self).

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"sgt {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # DECLARAÇÃO DE VARIÁVEL
    # =========================================================

    def visitDecl_Interna_Var_Tipo_Retorno_Expr(
        self,
        node
    ):

        nome = node.id

        value = node.expr.accept(self)

        self.store_variable(
            nome,
            value
        )

        return value


    def visitDecl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(
        self,
        node
    ):

        nome = node.id

        value = node.expr.accept(self)

        self.store_variable(
            nome,
            value
        )

        if node.decl_interna is not None:
            node.decl_interna.accept(self)

        return value


    # =========================================================
    # ATRIBUIÇÃO =
    # =========================================================

    def visitDecl_Interna_Equal_Expr(
        self,
        node
    ):

        value = node.expr.accept(self)

        self.store_variable(
            node.id,
            value
        )


    # =========================================================
    # ATRIBUIÇÃO +=
    # =========================================================

    def visitDecl_Interna_PlusEqual_Expr(
        self,
        node
    ):

        old_value = self.load_variable(node.id)

        value = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"add {result}, {old_value}, {value}"
        )

        self.store_variable(
            node.id,
            result
        )


    # =========================================================
    # ATRIBUIÇÃO -=
    # =========================================================

    def visitDecl_Interna_MinusEqual_Expr(
        self,
        node
    ):

        old_value = self.load_variable(node.id)

        value = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"sub {result}, {old_value}, {value}"
        )

        self.store_variable(
            node.id,
            result
        )


    # =========================================================
    # IF
    # =========================================================

    def visitDecl_Interna_If_Expr_Decl_Interna(
        self,
        node
    ):

        condition = node.expr.accept(self)

        false_label = self.new_label("if_false")
        end_label = self.new_label("if_end")

        self.emit(
            f"beq {condition}, $zero, {false_label}"
        )

        if node.decl_interna is not None:
            node.decl_interna.accept(self)

        self.emit(
            f"j {end_label}"
        )

        self.emit(
            f"{false_label}:"
        )

        self.emit(
            f"{end_label}:"
        )


    # =========================================================
    # IF COM ELSE
    # =========================================================

    def visitDecl_Interna_If_Expr_Decl_Interna_Decl_Interna(
        self,
        node
    ):

        condition = node.expr.accept(self)

        else_label = self.new_label("else")
        end_label = self.new_label("if_end")

        self.emit(
            f"beq {condition}, $zero, {else_label}"
        )

        # ATENÇÃO:
        # Esta classe possui decl_interna1 e decl_interna2.
        # decl_interna1 = bloco do IF
        # decl_interna2 = bloco do ELSE

        if node.decl_interna1 is not None:
            node.decl_interna1.accept(self)

        self.emit(
            f"j {end_label}"
        )

        self.emit(
            f"{else_label}:"
        )

        if node.decl_interna2 is not None:
            node.decl_interna2.accept(self)

        self.emit(
            f"{end_label}:"
        )


    # =========================================================
    # WHILE
    # =========================================================

    def visitDecl_Interna_While_Expr_Decl_Interna(
        self,
        node
    ):

        start_label = self.new_label("while")
        end_label = self.new_label("while_end")

        self.emit(
            f"{start_label}:"
        )

        condition = node.expr.accept(self)

        self.emit(
            f"beq {condition}, $zero, {end_label}"
        )

        if node.decl_interna is not None:
            node.decl_interna.accept(self)

        self.emit(
            f"j {start_label}"
        )

        self.emit(
            f"{end_label}:"
        )


    # =========================================================
    # FOR
    # =========================================================

    def visitDecl_Interna_For_Decl_Interna(
        self,
        node
    ):

        start = node.integer1
        end = node.integer2

        register = self.get_temp()

        self.emit(
            f"li {register}, {start}"
        )

        self.store_variable(
            node.id,
            register
        )

        start_label = self.new_label("for")
        end_label = self.new_label("for_end")

        self.emit(
            f"{start_label}:"
        )

        current = self.load_variable(node.id)

        limit = self.get_temp()

        self.emit(
            f"li {limit}, {end}"
        )

        condition = self.get_temp()

        self.emit(
            f"blt {current}, {limit}, {condition}"
        )

        self.emit(
            f"beq {condition}, $zero, {end_label}"
        )

        if node.decl_interna is not None:
            node.decl_interna.accept(self)

        current = self.load_variable(node.id)

        one = self.get_temp()

        self.emit(
            f"li {one}, 1"
        )

        incremented = self.get_temp()

        self.emit(
            f"add {incremented}, {current}, {one}"
        )

        self.store_variable(
            node.id,
            incremented
        )

        self.emit(
            f"j {start_label}"
        )

        self.emit(
            f"{end_label}:"
        )


    # =========================================================
    # CONSTANTES
    # =========================================================

    def visitDecl_Interna_Const_Expr(
        self,
        node
    ):

        value = node.expr.accept(self)

        self.store_variable(
            node.id,
            value
        )


    def visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(
        self,
        node
    ):

        value = node.expr.accept(self)

        self.store_variable(
            node.id,
            value
        )

        if node.decl_interna is not None:
            node.decl_interna.accept(self)


    # =========================================================
    # BREAK
    # =========================================================

    def visitDecl_Interna_Break_Decl_Interna(
        self,
        node
    ):

        pass


    # =========================================================
    # EXPRESSÕES BOOLEANAS
    # =========================================================

    def visitExpr_Expr_Equal_Equal_Expr(
        self,
        node
    ):

        left = node.expr1.accept(self)

        right = node.expr2.accept(self)

        result = self.get_temp()

        self.emit(
            f"seq {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # DIFERENTE
    # =========================================================

    def visitExpr_Expr_Exclamationmark_Equal_Expr(
        self,
        node
    ):

        left = node.expr1.accept(self)

        right = node.expr2.accept(self)

        result = self.get_temp()

        self.emit(
            f"sne {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # MENOR <
    # =========================================================

    def visitExpr_Id_Larrow_Expr(
        self,
        node
    ):

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"slt {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # MAIOR OU IGUAL >=
    # =========================================================

    def visitExpr_Id_RarrowEqual_Expr(
        self,
        node
    ):

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"sge {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # MENOR OU IGUAL <=
    # =========================================================

    def visitExpr_Id_LarrowEqual_Expr(
        self,
        node
    ):

        left = self.load_variable(node.id)

        right = node.expr.accept(self)

        result = self.get_temp()

        self.emit(
            f"sle {result}, {left}, {right}"
        )

        return result


    # =========================================================
    # RETORNO
    # =========================================================

    def visitDecl_Interna_Return_Expr(
        self,
        node
    ):

        value = node.expr.accept(self)

        self.emit(
            f"move $v0, {value}"
        )

        if self.current_function is not None:

            self.emit(
                f"j {self.current_function}_end"
            )


    # =========================================================
    # STRING
    # =========================================================

    def visitExpr_String(self, node):

        label = self.new_label("str")

        value = node.string

        self.emit_data(
            f'{label}: .asciiz {value}'
        )

        register = self.get_temp()

        self.emit(
            f"la {register}, {label}"
        )

        return register


    # =========================================================
    # BUILTIN IDENTIFIER
    # =========================================================

    def visitExpr_BuiltinIdentifier_Expr(
        self,
        node
    ):

        return node.expr.accept(self)


    # =========================================================
    # OPERAÇÕES NÃO IMPLEMENTADAS
    # =========================================================

    def visitArgs_String(self, node):
        pass


    def visitArgs_String_Args(self, node):
        pass


    def visitExpr_BuiltinIdentifier_String(self, node):
        pass


    def visitFuncao_Fn_Params_Tipo_Retorno(self, node):
        pass


    def visitFuncao_Pub_Fn_Params_Tipo_Retorno(self, node):
        pass


    def visitDecl_Const_Expr(self, node):
        pass


    def visitDecl_Const_Tipo_Retorno_Expr(self, node):
        pass


    def visitDecl_Equal_Expr(self, node):
        pass


    def visitDecl_Expr(self, node):
        pass


    def visitDecl_Var_Tipo_Retorno_Expr(self, node):
        pass


    def visitDecl_Interna_Const_Expr_Decl_Interna(self, node):
        pass


    def visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_Equal_Expr_Decl_Interna(self, node):
        pass


    def visitDecl_Interna_MinusEqual_Expr_Decl_Interna(self, node):
        pass


    def visitDecl_Interna_MinusPercentEqual_Expr(self, node):
        pass


    def visitDecl_Interna_MinusPercentEqual_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_MinusPercent_Expr(self, node):
        pass


    def visitDecl_Interna_MinusPercent_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_MinusPipeEqual_Expr(self, node):
        pass


    def visitDecl_Interna_MinusPipeEqual_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_MinusPipe_Expr(self, node):
        pass


    def visitDecl_Interna_MinusPipe_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_PlusEqual_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_PlusPercentEqual_Expr(self, node):
        pass


    def visitDecl_Interna_PlusPercentEqual_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_PlusPercent_Expr(self, node):
        pass


    def visitDecl_Interna_PlusPercent_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_PlusPipeEqual_Expr(self, node):
        pass


    def visitDecl_Interna_PlusPipeEqual_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Interna_PlusPipe_Expr(self, node):
        pass


    def visitDecl_Interna_PlusPipe_Expr_Decl_Interna(
        self,
        node
    ):
        pass


    def visitDecl_Id_MinusEqual_Expr(self, node):
        pass


    def visitDecl_Id_MinusPercentEqual_Expr(self, node):
        pass


    def visitDecl_Id_MinusPercent_Expr(self, node):
        pass


    def visitDecl_Id_MinusPipeEqual_Expr(self, node):
        pass


    def visitDecl_Id_MinusPipe_Expr(self, node):
        pass


    def visitDecl_Id_PlusEqual_Expr(self, node):
        pass


    def visitDecl_Id_PlusPercentEqual_Expr(self, node):
        pass


    def visitDecl_Id_PlusPercent_Expr(self, node):
        pass


    def visitDecl_Id_PlusPipeEqual_Expr(self, node):
        pass


    def visitDecl_Id_PlusPipe_Expr(self, node):
        pass


# =============================================================
# MAIN
# =============================================================

def main():

    f = open(
        "ex/exemplo.zig",
        "r"
    )

    lexer = lex.lex()

    lexer.input(
        f.read()
    )

    parser = yacc.yacc(
        module=ExpressionLanguageParser
    )

    result = parser.parse(
        debug=False,
        lexer=lexer
    )

    visitor = AssemblyVisitor()

    result.accept(visitor)

    print(
        "\n========== MIPS ASSEMBLY ==========\n"
    )

    print(
        visitor.generate()
    )

    with open("assembly.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(visitor.generate())
if __name__ == "__main__":
    main()

