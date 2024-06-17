# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
'''
## Ejercicio
 * comentario con la URL a Python.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"'''

# https://www.python.org/

# comentarios

# una linea con "#"

'''varias lineas con 
3 comillas (pueden ser simples o dobles)'''

"""varias lineas con 
3 comillas (pueden ser simples o dobles"""


# variables

"""por convencion las variables tienen nombres en minuscula con guion bajo para separar las 
palabras (snake)"""
variable_ejemplo_entera = 10
variable_ejemplo_entera = 10+1
# por convencion las constrantes van en mayusculas
CONSTANTE = 10

# tipos de datos

var_int: int
var_char: str
var_bool: bool
var_float: float

LENGUAJE_FAVORITO = 'Python'
print(f"¡Hola, {LENGUAJE_FAVORITO}!")
