# #01 OPERADORES Y ESTRUCTURAS DE CONTROL

#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

# Operadores Aritméticos

# operaciones basicas(+ : Suma,- : Resta,* : Multiplicación,/ : División)
var = 10 + 2 - 2 * 3 / 3

# otros 
# % : Módulo (residuo de la división)
var = 10 % 2 # da cero
# ** : Exponente (potencia)
var = 2 ** 2 # da cuatro
# // : División entera (retorna el cociente sin la parte decimal)
var = 3//2 # da 1

# Operadores lógicos
x = True
y = False
print(x and y)  # False
print(x or y)  # True
print(not x)  # False

# Operadores de comparación
a = 10
b = 3
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# Operadores de asignación
c = 5
c += 3  # c = c + 3
print(c)  # 8

# Operadores de identidad
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print(d is e)  # True
print(d is f)  # False
print(d is not f)  # True

#  tipos de estructuras de control que existan
notas = [4,7,9,10]
# Condicionales
promedio = (notas[0] + notas[1] + notas[2] + notas[3] )/4
if promedio> 6:
    print("aprobo con ", promedio)

# iterativas
# for
sumatoria = 0
for i in notas:
    sumatoria += i
print("nota promedio for", sumatoria/len(notas))

# while
nota = 0
sumatoria = 0
while nota < len(notas):
    sumatoria += notas[nota]
    nota +=1
print("nota promedio while ", sumatoria/len(notas))

# excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")


#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
print("numeros pares,entre 10 y 55 excepto el 16 y los multiplos de 3")

for i in range(10,56,2):
    if i != 16 and i % 3 != 0:
        print (i)