import ply.lex as lex

# resultado del análisis léxico
resultado_lexema = []

# Palabras reservadas
reservadas = (
    'mientras', 'para', 'desde', 'hasta', 'en',
    'si', 'sino', 'clase',
    'entero', 'gran_entero', 'real', 'gran_real', 'texto', 'caracter'
)

# Tokens
tokens = reservadas + (
    # Operadores aritméticos
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'DIVISION_ENTERA', 'POTENCIA', 'EDIV', 'MOD',

    # Operadores relacionales
    'MENOR', 'MENOR_IGUAL', 'MAYOR', 'MAYOR_IGUAL', 'IGUAL',

    # Operadores lógicos
    'NO', 'Y', 'O',

    # Operadores de asignación
    'ASIGNAR', 'MAS_IGUAL', 'MENOS_IGUAL',

    # Símbolos
    'DOSPUNTOS', 'LLAIZQ', 'LLADER', 'CORCHIZQ', 'CORCHDER', 'PARIZQ', 'PARDER',

    # Separador de sentencias
    'SALTO_LINEA',

    # Identificadores
    'IDENTIFICADOR',

    # Valores de asignación
    'ENTERO', 'REAL', 'TEXTO', 'CARACTER'
)

# Expresiones regulares para tokens simples
t_SUMA = r'SUM'
t_RESTA = r'RES'
t_MULTIPLICACION = r'MUL'
t_DIVISION = r'DIV'
t_DIVISION_ENTERA = r'EDIV'
t_POTENCIA = 'POW'
t_MOD = r'MOD'

t_MENOR = r'MEN'
t_MENOR_IGUAL = r'MENI'
t_MAYOR = r'MAY'
t_MAYOR_IGUAL = r'MAYI'
t_IGUAL = r'ES'

t_NO = r'NO'
t_Y = r'Y'
t_O = r'O'

t_ASIGNAR = r'='
t_MAS_IGUAL = r'\+='
t_MENOS_IGUAL = r'-='
t_DOSPUNTOS = r':'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_PARIZQ = r'\('
t_PARDER = r'\)'



# Valores de asignación
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_TEXTO(t):
    r'".*"'
    t.value = t.value.strip('"')
    return t

def t_CARACTER(t):
    r"'.*'"
    t.value = t.value.strip("'")
    return t

# Identificador de variable
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    global resultado_lexema
    estado = "** Token no válido en la Línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), str(t.value),
                                                                                   str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Instanciamos el analizador léxico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        analizador.input(data)
        resultado_lexema.clear()
        while True:
            tok = analizador.token()
            if not tok:
                break
            estado = "Línea {:4} Tipo {:16} Valor {:16} Posición {:4}".format(str(tok.lineno), str(tok.type),
                                                                               str(tok.value), str(tok.lexpos))
            resultado_lexema.append(estado)
        print(resultado_lexema)
