# #02 FUNCIONES Y ALCANCE
#  * - Crea ejemplos de funciones básicas 
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""
Funciones definidas por el usuario
"""

# Simple
def greet():
    print("Hola, Python!")

greet()

# Con retorno
def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Valter")

# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hola", "Valter")
args_greet(name="Valter", greet="Hola")

# Con un argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Valter")
default_arg_greet()

# Con argumentos y return
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hola", "Valter"))

# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Valter", "Muller", "comunidad")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Valter",
    alias="Muller",
    age=36
)

"""
Funciones dentro de funciones
"""
def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""
print(len("Muller"))
print(type(36))
print("Muller".upper())

"""
Variables locales y globales
"""
global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()


# Crea una función que reciba dos parámetros str y retorne un int
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si número es múltiplo de 3, primer parámetro.
#  *   - Si número es múltiplo de 5, segundo parámetro.
#  *   - Si número es múltiplo de 3 y de 5, las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def imprimir_numeros(cadena1: str, cadena2: str)-> int:
    numeros =0
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print(cadena1, cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i%5 == 0:
            print (cadena2)
        else:
            print (i)
            numeros += 1
       
    return numeros

print("numeros impresos ", imprimir_numeros("esteban", "quito") )        