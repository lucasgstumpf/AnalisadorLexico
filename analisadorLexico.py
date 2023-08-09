import ply.lex as lex

# Lista de tokens
tokens = [
    'NUMERO',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
]

# Regras para tokens simples
t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'

# Regra para número (inteiro)
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Rastrear o número da linha e a coluna
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.column = 0

# Tratamento de erro (caracteres inválidos)
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Crie o analisador léxico
lexer = lex.lex()

def processaALexico(entrada):
    # Alimente a string de entrada para o analisador léxico
    lexer.input(entrada)

    # Tokenize a entrada e construa a tabela formatada
    tabela = f"| {'Token':<7} | {'Valor':<7} | {'Linha':<7} |\n"  # Cabeçalho da tabela

    while True:
        token = lexer.token()
        if not token:
            break
        linha = f"| {str(token.type):<7} | {str(token.value):<7} | {str(token.lineno):<7} |\n"
        tabela += linha

    return tabela  # Retornar a tabela formatada como uma string



