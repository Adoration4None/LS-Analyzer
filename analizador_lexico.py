import ply.lex as lex

# resultado del análisis léxico
resultado_lexema = []

# Palabras reservadas
reservadas = (
    'TRAER', 'DE',
    'SEA', 'UN', 'FIN',
    'CONSTANTE',
    'SI', 'SINO',
    'MIENTRAS', 'PARA', 'DESDE', 'HASTA', 'EN',
    'CLASE'
)

# Tokens
tokens = reservadas + (
    # Operadores aritméticos
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'DIVISION_ENTERA', 'POTENCIA', 'MODULO',

    # Incremento/Decremento
    'MENOSMENOS', 'MASMAS',

    # Operadores relacionales
    'MENOR', 'MENOR_IGUAL', 'MAYOR', 'MAYOR_IGUAL', 'IGUAL', 'DIFERENTE',

    # Operadores lógicos
    'NOT', 'AND', 'OR',

    # Operadores de asignación
    'ASIGNAR', 'MAS_IGUAL', 'MENOS_IGUAL',

    # Símbolos
    'COMA', 'PUNTO', 'DOSPUNTOS', 'LLAIZQ', 'LLADER', 'CORCHIZQ', 'CORCHDER', 'PARIZQ', 'PARDER',

    # Separador de sentencias
    # 'SALTO_LINEA',

    # Identificadores
    'IDENTIFICADOR', 'TIPO_ENTERO', 'TIPO_REAL', 'TIPO_TEXTO', 'TIPO_CARACTER', 'TIPO_BOOL',

    # Tipos de dato
    'ENTERO', 'REAL', 'TEXTO', 'CARACTER', 'BOOL'
)

# Expresiones regulares para tokens simples
t_MENOSMENOS = r'\-\-'
t_MASMAS = r'\+\+'

t_AND = r'Y'
t_OR = r'O'

t_ASIGNAR = r'='
t_MAS_IGUAL = r'\+\='
t_MENOS_IGUAL = r'\-\='

t_COMA = r'\,'
t_PUNTO = r'\.'
t_DOSPUNTOS = r'\:'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_PARIZQ = r'\('
t_PARDER = r'\)'


def t_TRAER(t):
    r'traer'
    return t

def t_DE(t):
    r'de'
    return t

def t_SEA(t):
    r'sea'
    return t

def t_UN(t):
    r'un'
    return t

def t_FIN(t):
    r'fin'
    return t

def t_CONSTANTE(t):
    r'constante'
    return t

def t_SUMA(t):
   r'SUM'
   return t

def t_RESTA(t):
   r'RES'
   return t

def t_MULTIPLICACION(t):
   r'MUL'
   return t

def t_DIVISION(t):
   r'DIV'
   return t

def t_DIVISION_ENTERA(t):
   r'EDIV'
   return t

def t_POTENCIA(t):
   r'POW'
   return t

def t_MODULO(t):
   r'MOD'
   return t

def t_MENOR(t):
   r'MEN'
   return t

def t_MENOR_IGUAL(t):
   r'MENI'
   return t

def t_MAYOR(t):
   r'MAY'
   return t

def t_MAYOR_IGUAL(t):
   r'MOD'
   return t

def t_IGUAL(t):
   r'ES'
   return t

def t_DIFERENTE(t):
   r'NO ES'
   return t

def t_NOT(t):
    r'NO'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_TIPO_ENTERO(t):
    r'entero'
    return t

def t_TIPO_REAL(t):
    r'real'
    return t

def t_TIPO_TEXTO(t):
    r'texto'
    return t

def t_TIPO_CARACTER(t):
    r'caracter'
    return t

def t_TIPO_BOOL(t):
    r'bool'
    return t

# Identificador de variable
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_TEXTO(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_CARACTER(t):
    r"'.*'"
    t.value = t.value.strip("'")
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

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

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
