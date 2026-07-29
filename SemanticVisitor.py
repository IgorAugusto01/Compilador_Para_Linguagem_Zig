from ast import expr

from AbstractVisitor import AbstractVisitor
from Visitor import *
import Tabela_Simbolos as st
from ExpressionLanguageLex import *
import ExpressionLanguageParser 
import ply.yacc as yacc




class SemanticVisitor(Visitor):


    def __init__(self):
       
         self.data = []
         self.text = []

         
         self.current_function = None

        
         self.symbols = {}

         
         self.next_offset = -4

         
         self.stack_size = 32

         # Labels
         self.label_counter = 0

         # Controle de loops
         self.loop_stack = []

         # Registradores temporários
         self.register_counter = 0

         # Último registrador produzido por uma expressão
         self.last_register = None

         # Controle de retorno
         self.return_label = None

    # ==========================================================
    # AUXILIARES
    # ==========================================================

def emit(self, instruction):
        self.text.append(instruction)

def emit_data(self, instruction):
        self.data.append(instruction)

def new_label(self, prefix="label"):
        label = f"{prefix}{self.label_counter}"
        self.label_counter += 1
        return label

def new_register(self):
        """
        Retorna registradores temporários $t0-$t9 em esquema circular.
        """

        reg = f"$t{self.register_counter % 10}"
        self.register_counter += 1
        return reg

def reset_registers(self):
        self.register_counter = 0

def get_id_name(self, obj):
        """
        Aceita:
            'x'
            Id('x')
            objetos que possuam .nome
            objetos que possuam .id
        """

        if obj is None:
            return None

        if isinstance(obj, str):
            return obj

        if hasattr(obj, "nome"):
            return obj.nome

        if hasattr(obj, "id"):
            value = obj.id

            if isinstance(value, str):
                return value

            if hasattr(value, "nome"):
                return value.nome

            if hasattr(value, "id"):
                return self.get_id_name(value)

        return str(obj)

def get_type_name(self, obj):
        if obj is None:
            return None

        if hasattr(obj, "tipo"):
            tipo = obj.tipo

            if isinstance(tipo, str):
                return tipo

            if hasattr(tipo, "tipo"):
                return tipo.tipo

        return str(obj)

def ensure_stack_space(self):
        """
        Reserva espaço suficiente para as variáveis locais.

        Os primeiros 32 bytes são preservados para:
            28($sp) -> $ra
            24($sp) -> $fp

        Variáveis começam em:
            -4($sp)
            -8($sp)
            ...
        """

        required = abs(self.next_offset) + 32

        if required > self.stack_size:
            self.stack_size = ((required + 15) // 16) * 16

def declare_variable(self, name, tipo=None, const=False):
        """
        Declara uma variável somente uma vez.
        """

        if name is None:
            return None

        if name in self.symbols:
            return self.symbols[name]["offset"]

        offset = self.next_offset
        self.next_offset -= 4

        self.symbols[name] = {
            "offset": offset,
            "type": self.get_type_name(tipo),
            "const": const
        }

        self.ensure_stack_space()

        return offset

def get_offset(self, name):
        name = self.get_id_name(name)

        if name not in self.symbols:
            raise Exception(
                f"Erro semântico: variável '{name}' "
                f"não foi declarada."
            )

        return self.symbols[name]["offset"]

def variable_exists(self, name):
        name = self.get_id_name(name)
        return name in self.symbols

def load_variable(self, name):
        """
        Gera:

            lw $tX, offset($sp)

        e retorna o registrador.
        """

        name = self.get_id_name(name)
        offset = self.get_offset(name)

        reg = self.new_register()

        self.emit(f"lw {reg}, {offset}($sp)")

        return reg

def store_variable(self, name, register):
        """
        Armazena o conteúdo de register na variável.
        """

        name = self.get_id_name(name)
        offset = self.get_offset(name)

        if register is None:
            raise Exception(
                f"Erro interno: tentativa de armazenar None "
                f"na variável '{name}'."
            )

        self.emit(f"sw {register}, {offset}($sp)")

def store_immediate(self, name, value):
        """
        Declara e inicializa uma variável com valor imediato.
        """

        if not self.variable_exists(name):
            self.declare_variable(name)

        reg = self.new_register()
        self.emit(f"li {reg}, {value}")
        self.store_variable(name, reg)

        return reg

def visit_child(self, child):
        if child is None:
            return None

        result = child.accept(self)

        if result is not None:
            self.last_register = result

        return result

    # ==========================================================
    # PROGRAMA
    # ==========================================================

def visitPrograma_Funcao(self, node):
        return node.funcao.accept(self)

def visitPrograma_Decl(self, node):
        return node.decl.accept(self)

def visitPrograma_Funcao_Programa(self, node):
        node.funcao.accept(self)
        node.programa.accept(self)

def visitPrograma_Decl_Programa(self, node):
        node.decl.accept(self)
        node.programa.accept(self)

    # ==========================================================
    # FUNÇÕES
    # ==========================================================

def start_function(self, name):
        self.current_function = name

        self.symbols = {}
        self.next_offset = -4
        self.stack_size = 32
        self.reset_registers()

        self.return_label = self.new_label("function_return")

        self.emit("")
        self.emit(f"{name}:")
        self.emit(f"addi $sp, $sp, -{self.stack_size}")
        self.emit(f"sw $ra, {self.stack_size - 4}($sp)")
        self.emit(f"sw $fp, {self.stack_size - 8}($sp)")
        self.emit("move $fp, $sp")

def finish_function(self):
        self.emit("")
        self.emit(f"{self.return_label}:")

        self.emit("move $sp, $fp")
        self.emit(f"lw $fp, {self.stack_size - 8}($sp)")
        self.emit(f"lw $ra, {self.stack_size - 4}($sp)")
        self.emit(f"addi $sp, $sp, {self.stack_size}")
        self.emit("jr $ra")

        self.current_function = None

def visitFuncao_Pub_Fn_Params_Tipo_Retorno_Decl_Interna(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.process_params(node.params)

        self.visit_child(node.decl_interna)

        self.finish_function()

def visitFuncao_Pub_Fn_Tipo_Retorno_Decl_Interna(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.visit_child(node.decl_interna)

        self.finish_function()

def visitFuncao_Fn_Params_Tipo_Retorno_Decl_Interna(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.process_params(node.params)

        self.visit_child(node.decl_interna)

        self.finish_function()

def visitFuncao_Fn_Tipo_Retorno_Decl_Interna(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.visit_child(node.decl_interna)

        self.finish_function()

def visitFuncao_Pub_Fn_Params_Tipo_Retorno(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.process_params(node.params)

        self.finish_function()

def visitFuncao_Fn_Params_Tipo_Retorno(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.process_params(node.params)

        self.finish_function()

def visitFuncao_Pub_Fn_Tipo_Retorno(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.finish_function()

def visitFuncao_Fn_Tipo_Retorno(self, node):
        name = self.get_id_name(node.id)

        self.start_function(name)

        self.finish_function()

def process_params(self, params):
        """
        Processa parâmetros recursivamente.

        Como a AST não guarda explicitamente a posição dos
        parâmetros nos registradores, eles são copiados para
        variáveis locais.

        Convenção utilizada:
            $a0, $a1, $a2, $a3
        """

        current = params
        arg_register = 0

        while current is not None:

            if hasattr(current, "id"):
                name = self.get_id_name(current.id)
            else:
                break

            tipo = getattr(current, "tipo_retorno", None)

            if not self.variable_exists(name):
                self.declare_variable(name, tipo)

            if arg_register <= 3:
                self.emit(
                    f"sw $a{arg_register}, "
                    f"{self.get_offset(name)}($sp)"
                )

            if hasattr(current, "params"):
                current = current.params
            else:
                current = None

            arg_register += 1

    # ==========================================================
    # ID
    # ==========================================================

def visitId(self, node):
        return self.get_id_name(node)

    # ==========================================================
    # TIPOS
    # ==========================================================

def visitTipo_Retorno(self, node):
        return self.get_type_name(node)

def visitTipo(self, node):
        return self.get_type_name(node)

    # ==========================================================
    # PARAMETROS
    # ==========================================================

def visitParams_Id_Tipo_Retorno(self, node):
        return node

def visitParams_Id_Tipo_Retorno_Params(self, node):
        return node

    # ==========================================================
    # DECLARAÇÕES EXTERNAS
    # ==========================================================

def visitDecl_Var_Tipo_Retorno_Expr(self, node):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            node.tipo_retorno,
            const=False
        )

        reg = self.visit_child(node.expr)

        if reg is None:
            raise Exception(
                f"Erro: expressão da variável '{name}' "
                f"não produziu registrador."
            )

        self.store_variable(name, reg)

        return reg

def visitDecl_Const_Expr(self, node):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            const=True
        )

        reg = self.visit_child(node.expr)

        if reg is None:
            raise Exception(
                f"Erro: expressão da constante '{name}' "
                f"não produziu registrador."
            )

        self.store_variable(name, reg)

        return reg

def visitDecl_Const_Tipo_Retorno_Expr(self, node):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            node.tipo_retorno,
            const=True
        )

        reg = self.visit_child(node.expr)

        if reg is None:
            raise Exception(
                f"Erro: expressão da constante '{name}' "
                f"não produziu registrador."
            )

        self.store_variable(name, reg)

        return reg

def visitDecl_Equal_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        reg = self.visit_child(node.expr)

        self.store_variable(name, reg)

        return reg

def visitDecl_Expr(self, node):
        return self.visit_child(node.expr)

def visitDecl_Id_PlusEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"add {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_PlusPercent_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"or {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_PlusPercentEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"or {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_PlusPipe_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"or {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_PlusPipeEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"or {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_MinusEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"sub {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_MinusPercent_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"and {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_MinusPercentEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"and {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_MinusPipe_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"and {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

def visitDecl_Id_MinusPipeEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"and {result}, {left}, {right}")

        self.store_variable(name, result)

        return result

    # ==========================================================
    # EXPRESSÕES
    # ==========================================================

def visitBuiltinIdentifier(self, node):
        return self.get_id_name(node)

def visitExpr_BuiltinIdentifier_String(self, node):

        name = self.get_id_name(node.builtindentifier)

        string_value = getattr(node, "string", "")

        label = self.new_label("str")

        self.emit_data(f'{label}: .asciiz "{string_value}"')

        reg = self.new_register()

        self.emit(f"la {reg}, {label}")

        return reg

def visitExpr_BuiltinIdentifier_Expr(self, node):

        left = self.visit_child(node.expr1)
        right = self.visit_child(node.expr2)

        result = self.new_register()

        # Operação genérica.
        # O builtin pode ser tratado posteriormente conforme
        # a especificação da linguagem.

        self.emit(f"add {result}, {left}, {right}")

        return result

def visitExpr_Expr_Plus_Expr(self, node):

        left = self.visit_child(node.expr1)
        right = self.visit_child(node.expr2)

        result = self.new_register()

        self.emit(f"add {result}, {left}, {right}")

        return result

def visitExpr_Expr_Minus_Expr(self, node):

        left = self.visit_child(node.expr1)
        right = self.visit_child(node.expr2)

        result = self.new_register()

        self.emit(f"sub {result}, {left}, {right}")

        return result

def visitExpr_Expr_Asterisk_Expr(self, node):

        left = self.visit_child(node.expr1)
        right = self.visit_child(node.expr2)

        result = self.new_register()

        self.emit(f"mul {result}, {left}, {right}")

        return result

def visitExpr_Id(self, node):

        name = self.get_id_name(node.id)

        return self.load_variable(name)

def visitExpr_Id_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"add {result}, {left}, {right}")

        return result

def visitExpr_Call(self, node):

        return self.visit_child(node.call)

def visitExpr_Integer(self, node):

        value = node.integer

        reg = self.new_register()

        self.emit(f"li {reg}, {value}")

        return reg

def visitExpr_Id_Slash_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"div {left}, {right}")
        self.emit(f"mflo {result}")

        return result

def visitExpr_Id_Rarrow_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"sgt {result}, {left}, {right}")

        return result

def visitExpr_Id_Larrow_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"slt {result}, {left}, {right}")

        return result

def visitExpr_Id_Percent_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"div {left}, {right}")
        self.emit(f"mfhi {result}")

        return result

def visitExpr_Id_EqualEqual_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"sub {result}, {left}, {right}")
        self.emit(f"sltiu {result}, {result}, 1")

        return result

def visitExpr_Id_And_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"and {result}, {left}, {right}")

        return result

def visitExpr_Id_Or_Expr(self, node):

        name = self.get_id_name(node.id)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(f"or {result}, {left}, {right}")

        return result

def visitExpr_True(self, node):

        reg = self.new_register()

        self.emit(f"li {reg}, 1")

        return reg

def visitExpr_False(self, node):

        reg = self.new_register()

        self.emit(f"li {reg}, 0")

        return reg

    # ==========================================================
    # CALL
    # ==========================================================

def visitCall_Args(self, node):

        name = self.get_id_name(node.id)

        args = []
        current = node.args

        self.collect_args(current, args)

        for i, arg in enumerate(args):

            if i > 3:
                break

            reg = self.visit_child(arg)

            self.emit(f"move $a{i}, {reg}")

        self.emit(f"jal {name}")

        result = self.new_register()

        self.emit(f"move {result}, $v0")

        return result

def visitCall_No_Args(self, node):

        name = self.get_id_name(node.id)

        self.emit(f"jal {name}")

        result = self.new_register()

        self.emit(f"move {result}, $v0")

        return result

def collect_args(self, node, result):

        if node is None:
            return

        if node.__class__.__name__ == "Args_Id":
            result.append(
                self.make_fake_expr_id(node.id)
            )
            return

        if node.__class__.__name__ == "Args_Id_Args":
            result.append(
                self.make_fake_expr_id(node.id)
            )
            self.collect_args(node.args, result)
            return

        if node.__class__.__name__ == "Args_String":
            result.append(node)
            return

        if node.__class__.__name__ == "Args_String_Args":
            result.append(node)
            self.collect_args(node.args, result)

def make_fake_expr_id(self, value):

        class FakeId:
            pass

        class FakeExpr:
            pass

        ident = FakeId()
        ident.id = value

        expr = FakeExpr()
        expr.id = value



def visitArgs_Id(self, node):
        return self.load_variable(
            self.get_id_name(node.id)
        )

def visitArgs_Id_Args(self, node):
        return self.load_variable(
            self.get_id_name(node.id)
        )

def visitArgs_String(self, node):

        value = getattr(node, "string", "")

        label = self.new_label("string")

        self.emit_data(
            f'{label}: .asciiz "{value}"'
        )

        reg = self.new_register()

        self.emit(f"la {reg}, {label}")

        return reg

def visitArgs_String_Args(self, node):

        value = getattr(node, "string", "")

        label = self.new_label("string")

        self.emit_data(
            f'{label}: .asciiz "{value}"'
        )

        reg = self.new_register()

        self.emit(f"la {reg}, {label}")

        return reg

    # ==========================================================
    # DECLARAÇÕES INTERNAS
    # ==========================================================

def visitDecl_Interna_Break(self, node):

        if not self.loop_stack:
            raise Exception(
                "Erro semântico: 'break' fora de um loop."
            )

        self.emit(
            f"j {self.loop_stack[-1]}"
        )

def visitDecl_Interna_Return_Expr(self, node):

        reg = self.visit_child(node.expr)

        self.emit(f"move $v0, {reg}")

        self.emit(
            f"j {self.return_label}"
        )

        return reg

    # ==========================================================
    # WHILE
    # ==========================================================

def visitDecl_Interna_While_Expr_Decl_Interna(self, node):

        condition_label = self.new_label("while")
        end_label = self.new_label("while_end")

        self.emit(f"{condition_label}:")

        condition = self.visit_child(node.expr)

        self.emit(
            f"beq {condition}, $zero, {end_label}"
        )

        self.loop_stack.append(end_label)

        self.visit_child(node.decl_interna)

        self.loop_stack.pop()

        self.emit(
            f"j {condition_label}"
        )

        self.emit(f"{end_label}:")

def visitDecl_Interna_While_Expr_Decl_Interna_Decl_Interna(
        self,
        node
    ):

        condition_label = self.new_label("while")
        end_label = self.new_label("while_end")

        self.emit(f"{condition_label}:")

        condition = self.visit_child(node.expr)

        self.emit(
            f"beq {condition}, $zero, {end_label}"
        )

        self.loop_stack.append(end_label)

        self.visit_child(node.decl_interna1)

        self.loop_stack.pop()

        self.emit(
            f"j {condition_label}"
        )

        self.emit(f"{end_label}:")

        self.visit_child(node.decl_interna2)

    # ==========================================================
    # FOR
    # ==========================================================

def visitDecl_Interna_For_Decl_Interna(self, node):

        start = int(node.integer1)
        end = int(node.integer2)
        name = self.get_id_name(node.id)

        if not self.variable_exists(name):
            self.declare_variable(name)

        reg = self.new_register()

        self.emit(f"li {reg}, {start}")
        self.store_variable(name, reg)

        condition_label = self.new_label("for")
        end_label = self.new_label("for_end")

        self.emit(f"{condition_label}:")

        current = self.load_variable(name)

        limit = self.new_register()

        self.emit(f"li {limit}, {end}")

        condition = self.new_register()

        self.emit(
            f"slt {condition}, {current}, {limit}"
        )

        self.emit(
            f"beq {condition}, $zero, {end_label}"
        )

        self.loop_stack.append(end_label)

        self.visit_child(node.decl_interna)

        self.loop_stack.pop()

        current = self.load_variable(name)

        one = self.new_register()

        self.emit(f"li {one}, 1")

        incremented = self.new_register()

        self.emit(
            f"add {incremented}, {current}, {one}"
        )

        self.store_variable(
            name,
            incremented
        )

        self.emit(
            f"j {condition_label}"
        )

        self.emit(f"{end_label}:")

def visitDecl_Interna_For_Decl_Interna_Decl_Interna(
        self,
        node
    ):

    start = int(node.integer1)
    end = int(node.integer2)
    name = self.get_id_name(node.id)

    if not self.variable_exists(name):
        self.declare_variable(name)

    reg = self.new_register()

    self.emit(f"li {reg}, {start}")
    self.store_variable(name, reg)

    condition_label = self.new_label("for")
    end_label = self.new_label("for_end")

    self.emit(f"{condition_label}:")

    current = self.load_variable(name)

    limit = self.new_register()

    self.emit(f"li {limit}, {end}")

    condition = self.new_register()

    self.emit(
        f"slt {condition}, {current}, {limit}"
    )

    self.emit(
        f"beq {condition}, $zero, {end_label}"
    )

    self.loop_stack.append(end_label)

    self.visit_child(node.decl_interna1)

    self.loop_stack.pop()

    current = self.load_variable(name)

    one = self.new_register()

    self.emit(f"li {one}, 1")

    incremented = self.new_register()

    self.emit(
        f"add {incremented}, {current}, {one}"
    )

    self.store_variable(
        name,
        incremented
    )

    self.emit(
        f"j {condition_label}"
    )

    self.emit(f"{end_label}:")

    self.visit_child(node.decl_interna2)

# ==========================================================
# IF
# ==========================================================

def visitDecl_Interna_If_Expr_Decl_Interna(
        self,
        node
    ):

        else_label = self.new_label("else")
        end_label = self.new_label("if_end")

        condition = self.visit_child(node.expr)

        self.emit(
            f"beq {condition}, $zero, {else_label}"
        )

        self.visit_child(node.decl_interna)

        self.emit(
            f"j {end_label}"
        )

        self.emit(f"{else_label}:")

        self.emit(f"{end_label}:")

def visitDecl_Interna_If_Expr_Decl_Interna_Decl_Interna(
        self,
        node
    ):

        else_label = self.new_label("else")
        end_label = self.new_label("if_end")

        condition = self.visit_child(node.expr)

        self.emit(
            f"beq {condition}, $zero, {else_label}"
        )

        self.visit_child(node.decl_interna1)

        self.emit(
            f"j {end_label}"
        )

        self.emit(f"{else_label}:")

        self.visit_child(node.decl_interna2)

        self.emit(f"{end_label}:")

    # ==========================================================
    # DECLARAÇÕES INTERNAS DE VARIÁVEIS
    # ==========================================================

def visitDecl_Interna_Var_Tipo_Retorno_Expr(self, node):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            node.tipo_retorno,
            False
        )

        reg = self.visit_child(node.expr)

        self.store_variable(name, reg)

        return reg

def visitDecl_Interna_Const_Expr(self, node):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            const=True
        )

        reg = self.visit_child(node.expr)

        self.store_variable(name, reg)

        return reg

def visitDecl_Interna_Const_Tipo_Retorno_Expr(
        self,
        node
    ):

        name = self.get_id_name(node.id)

        self.declare_variable(
            name,
            node.tipo_retorno,
            True
        )

        reg = self.visit_child(node.expr)

        self.store_variable(name, reg)

        return reg

def visitDecl_Interna_Var_Tipo_Retorno_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_Var_Tipo_Retorno_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_Const_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_Const_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_Const_Tipo_Retorno_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_Const_Tipo_Retorno_Expr(node)

        self.visit_child(node.decl_interna)

        return result

    # ==========================================================
    # ATRIBUIÇÕES INTERNAS
    # ==========================================================

def check_assignment(self, name):

        name = self.get_id_name(name)

        if not self.variable_exists(name):
            raise Exception(
                f"Erro semântico: variável '{name}' "
                f"não foi declarada."
            )

        if self.symbols[name]["const"]:
            raise Exception(
                f"Erro semântico: '{name}' é constante "
                f"e não pode ser alterada."
            )

def assignment_binary(
        self,
        node,
        operation
    ):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        left = self.load_variable(name)
        right = self.visit_child(node.expr)

        result = self.new_register()

        self.emit(
            f"{operation} {result}, {left}, {right}"
        )

        self.store_variable(name, result)

        return result

def visitDecl_Interna_Equal_Expr(self, node):

        name = self.get_id_name(node.id)

        self.check_assignment(name)

        result = self.visit_child(node.expr)

        self.store_variable(name, result)

        return result

def visitDecl_Interna_PlusEqual_Expr(self, node):
        return self.assignment_binary(node, "add")

def visitDecl_Interna_PlusPercent_Expr(self, node):
        return self.assignment_binary(node, "or")

def visitDecl_Interna_PlusPercentEqual_Expr(self, node):
        return self.assignment_binary(node, "or")

def visitDecl_Interna_PlusPipe_Expr(self, node):
        return self.assignment_binary(node, "or")

def visitDecl_Interna_PlusPipeEqual_Expr(self, node):
        return self.assignment_binary(node, "or")

def visitDecl_Interna_MinusEqual_Expr(self, node):
        return self.assignment_binary(node, "sub")

def visitDecl_Interna_MinusPercent_Expr(self, node):
        return self.assignment_binary(node, "and")

def visitDecl_Interna_MinusPercentEqual_Expr(self, node):
        return self.assignment_binary(node, "and")

def visitDecl_Interna_MinusPipe_Expr(self, node):
        return self.assignment_binary(node, "and")

def visitDecl_Interna_MinusPipeEqual_Expr(self, node):
        return self.assignment_binary(node, "and")

    # ==========================================================
    # ATRIBUIÇÕES + DECL_INTERNA
    # ==========================================================

def visitDecl_Interna_Equal_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_Equal_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_PlusEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_PlusEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_PlusPercent_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_PlusPercent_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_PlusPercentEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_PlusPercentEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_PlusPipe_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_PlusPipe_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_PlusPipeEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_PlusPipeEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_MinusEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_MinusEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_MinusPercent_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_MinusPercent_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_MinusPercentEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_MinusPercentEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_MinusPipe_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_MinusPipe_Expr(node)

        self.visit_child(node.decl_interna)

        return result

def visitDecl_Interna_MinusPipeEqual_Expr_Decl_Interna(
        self,
        node
    ):

        result = self.visitDecl_Interna_MinusPipeEqual_Expr(node)

        self.visit_child(node.decl_interna)

        return result

    # ==========================================================
    # EXPRESSÃO INTERNA
    # ==========================================================

def visitDecl_Interna_Expr(self, node):
        return self.visit_child(node.expr)

def visitDecl_Interna_Expr_Decl_Interna(self, node):

        result = self.visit_child(node.expr)

        self.visit_child(node.decl_interna)

        return result

    # ==========================================================
    # BREAK + CONTINUAÇÃO
    # ==========================================================

def visitDecl_Interna_Break_Decl_Interna(
        self,
        node
    ):

        self.visitDecl_Interna_Break(node)

        self.visit_child(node.decl_interna)

    # ==========================================================
    # RETURN + CONTINUAÇÃO
    # ==========================================================

def visitDecl_Interna_Return_Expr_Decl_Interna(
        self,
        node
    ):

        reg = self.visit_child(node.expr)

        self.emit(f"move $v0, {reg}")

        self.emit(
            f"j {self.return_label}"
        )

        self.visit_child(node.decl_interna)

        return reg

    # ==========================================================
    # GERAÇÃO FINAL
    # ==========================================================

def generate(self):

        result = []

        result.append(".data")
        result.append("")

        for line in self.data:
            result.append(line)

        result.append("")
        result.append(".text")
        result.append(".globl main")
        result.append("")

        result.extend(self.text)

        return "\n".join(result)

def print_assembly(self):

        print(
            "\n========== MIPS ASSEMBLY ==========\n"
        )

        print(self.generate())
        print(
            "\n===================================\n"
        )

def main():
        f = open("ex/exemplo.zig", "r")

        lexer = lex.lex()
        lexer.input(f.read())

        parser = yacc.yacc(module=ExpressionLanguageParser)

        print("#imprime erros semanticos encontrados")

        svisitor = SemanticVisitor() 

        result = parser.parse(
            debug=False,
            lexer=lexer
        )

        result.accept(svisitor)

        print(f"Foram encontrados {svisitor.getnerros()} erros")


if __name__ == "__main__":
        main()