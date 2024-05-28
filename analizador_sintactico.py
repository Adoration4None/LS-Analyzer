import ply.yacc as yacc

from analizador_lexico import analizador, tokens

# Resultado del análisis gramatical
resultado_gramatica = []

precedence = (
    ('right','ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION_ENTERA'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUM expresion
                |   expresion RES expresion
                |   expresion MUL expresion
                |   expresion DIV expresion
                |   expresion POW expresion
                |   expresion MOD expresion
    '''
    if t[2] == 'SUM':
        t[0] = t[1] + t[3]
    elif t[2] == 'RES':
        t[0] = t[1] - t[3]
    elif t[2] == 'MUL':
        t[0] = t[1] * t[3]
    elif t[2] == 'DIV':
        t[0] = t[1] / t[3]
    elif t[2] == 'POW':
        t[0] = t[1] ** t[3]
    elif t[2] == 'MOD':
        t[0] = t[1] % t[3]

def p_expresion_uminus(t):
    'expresion : RES expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
                | LLAIZQ expresion LLADER
                | CORCHIZQ expresion CORCHDER
    '''
    t[0] = t[2]

def p_expresion_relacional(t):
    '''
    expresion   :   expresion MEN expresion
                |   expresion MENI expresion
                |   expresion MAY expresion
                |   expresion MAYI expresion
                |   expresion ES expresion
    '''
    if t[2] == "MEN":
        t[0] = t[1] < t[3]
    elif t[2] == "MENI":
        t[0] = t[1] <= t[3]
    elif t[2] == "MAY":
        t[0] = t[1] > t[3]
    elif t[2] == "MAYI":
        t[0] = t[1] >= t[3]
    elif t[2] == "ES":
        t[0] = t[1] == t[3]

def p_expresion_logica(t):
    '''
    expresion   :   expresion AND expresion
                |   expresion OR expresion
                |   NO expresion
    '''
    if t[2] == "Y":
        t[0] = t[1] and t[3]
    elif t[2] == "O":
        t[0] = t[1] or t[3]
    elif t[1] == "NO":
        t[0] = not t[2]

def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_cadena(t):
    'expresion : TEXTO'
    t[0] = t[1]

def p_expresion_caracter(t):
    'expresion : CARACTER'
    t[0] = t[1]

def p_expresion_identificador(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintáctico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintáctico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("Resultado: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        prueba_sintactica(s)