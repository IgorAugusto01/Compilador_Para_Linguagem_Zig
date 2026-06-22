import ply.lex as lex


palavras_reservadas= {
    'and': 'KEYWORD_AND',
    'anytype': 'KEYWORD_ANYTYPE',
    'break': 'KEYWORD_BREAK',
    'const': 'KEYWORD_CONST',
    'continue': 'KEYWORD_CONTINUE',
    'else': 'KEYWORD_ELSE',
    'enum': 'KEYWORD_ENUM',
    'false': 'KEYWORD_FALSE',
    'fn': 'KEYWORD_FN',
    'for': 'KEYWORD_FOR',
    'if': 'KEYWORD_IF',
    'or': 'KEYWORD_OR',
    'orelse': 'KEYWORD_ORELSE',
    'pub': 'KEYWORD_PUB',
    'return': 'KEYWORD_RETURN',
    'struct': 'KEYWORD_STRUCT',
    'switch': 'KEYWORD_SWITCH',
    'true': 'KEYWORD_TRUE',
    'union': 'KEYWORD_UNION',
    'undefined': 'KEYWORD_UNDEFINED',
    'while': 'KEYWORD_WHILE',
    'var': 'KEYWORD_VAR',
    'void': 'KEYWORD_VOID',
    'i8': 'KEYWORD_I8',
    'u8': 'KEYWORD_U8',
    'i16': 'KEYWORD_I16',
    'u16': 'KEYWORD_U16',
    'i32': 'KEYWORD_I32',
    'u32': 'KEYWORD_U32',
    'i64': 'KEYWORD_I64',
    'u64': 'KEYWORD_U64',
    'i128': 'KEYWORD_I128',
    'u128': 'KEYWORD_U128'

}

tokens =[
    'STRING',
    'LINE_COMMENT',
    'CHAR',
    'INTEGER',
    'ID',
    'BUILTINIDENTIFIER',
    'AMPERSAND',
    'AMPERSANDEQUAL',
    'ASTERISK',
    'ASTERISKEQUAL',
    'ASTERISKPERCENT',
    'ASTERISKPERCENTEQUAL',
    'CARET',
    'CARETEQUAL',
    'COLON',
    'COMMA',
    'DOT',
    'DOT2',
    'DOT3',
    'DOTASTERISK',
    'DOTQUESTIONMARK',
    'EQUAL',
    'EQUALEQUAL',
    'EQUALRARROW',
    'EXCLAMATIONMARK',
    'EXCLAMATIONMARKEQUAL',
    'LARROW',
    'LARROW2',
    'LARROW2EQUAL',
    'LARROW2PIPE',
    'LARROW2PIPEEQUAL',
    'LARROWEQUAL',
    'LBRACE',
    'LBRACKET',
    'LPAREN',
    'MINUS',
    'MINUSEQUAL',
    'MINUSPERCENT',
    'MINUSPERCENTEQUAL',
    'MINUSPIPE',
    'MINUSPIPEEQUAL',
    'MINUSRARROW',
    'PERCENT',
    'PERCENTEQUAL',
    'PIPE',
    'PIPE2',
    'PIPEEQUAL',
    'PLUS',
    'PLUS2',
    'PLUSEQUAL',
    'PLUSPERCENT',
    'PLUSPERCENTEQUAL',
    'PLUSPIPE',
    'PLUSPIPEEQUAL',
    'QUESTIONMARK',
    'RARROW',
    'RARROW2',
    'RARROW2EQUAL',
    'RARROWEQUAL',
    'RBRACE',
    'RBRACKET',
    'RPAREN',
    'SEMICOLON',
    'SLASH',
    'SLASHEQUAL',
    'TILDE'
] + list(palavras_reservadas.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = palavras_reservadas.get(t.value, 'ID')
    return t

def t_error(t):
    print("Caractere inválido:", t.value[0])
    t.lexer.skip(1)

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'

t_STRING = r'"([^"\\]|\\.)*"'

t_LINE_COMMENT = r'//[^\n]*'

t_CHAR = r"'.'"

def t_INTEGER(t):
    r'0b[01](_?[01]*)*|0o[0-7](_?[0-7]*)*|0x[a-fA-F0-9](_?[a-fA-F0-9]*)*|0|[1-9][0-9]*'
    t.value = int(t.value, 0)
    return t

t_BUILTINIDENTIFIER =r'@[a-zA-Z_][a-zA-Z0-9_]*'

t_AMPERSAND = r'&'

t_AMPERSANDEQUAL = '&='

t_ASTERISK =r'\*'

t_ASTERISKEQUAL = r'\*='

t_ASTERISKPERCENT = r'\*%'

t_ASTERISKPERCENTEQUAL = r'\*%='

t_CARET = r'\^'

t_CARETEQUAL = r'\^='

t_COLON= r":"

t_COMMA = r","

t_DOT3 = r"\.{3}"

t_DOT2 = r"\.{2}"

t_DOT = r"\."

t_DOTASTERISK = r"\.\*"

t_DOTQUESTIONMARK = r"\.\?"

t_EQUAL = r'='

t_EQUALEQUAL = r"=="

t_EQUALRARROW = r'=>'

t_EXCLAMATIONMARK = r'!'

t_EXCLAMATIONMARKEQUAL = r'!='

t_LARROW = r'<'

t_LARROW2 = r'<<'

t_LARROW2EQUAL = r'<<='

t_LARROW2PIPE = r'<<\|'

t_LARROW2PIPEEQUAL = r'<<\|='

t_LARROWEQUAL = r'<='

t_LBRACE = r'\{'

t_LBRACKET = r'\['

t_LPAREN = r'\('

t_MINUS = r'-'

t_MINUSEQUAL = r'-='

t_MINUSPERCENT = r'-%'

t_MINUSPERCENTEQUAL = r'-%='

t_MINUSPIPE = r'-\|'

t_MINUSPIPEEQUAL = r'-\|='

t_MINUSRARROW = r'->'

t_PERCENT = r'%'

t_PERCENTEQUAL = r'%='

t_PIPE = r'\|'

t_PIPE2 = r'\|\|'

t_PIPEEQUAL = r'\|='

t_PLUS = r'\+'

t_PLUS2 = r'\+\+'

t_PLUSEQUAL = r'\+='

t_PLUSPERCENT = r'\+%'

t_PLUSPERCENTEQUAL = r'\+%='

t_PLUSPIPE = r'\+\|'

t_PLUSPIPEEQUAL = r'\+\|='

t_QUESTIONMARK = r'\?'

t_RARROW = r'>'

t_RARROW2 = r'>>'

t_RARROW2EQUAL = r'>>='

t_RARROWEQUAL = r'>='

t_RBRACE = r'\}'

t_RBRACKET = r'\]'

t_RPAREN = r'\)'

t_SEMICOLON = r';'

t_SLASH = r'/'

t_SLASHEQUAL = r'/='

t_TILDE = r'~'






def main():
   f = open("exemplo.zig", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ =="__main__":
    main()
