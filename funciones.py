#Cree una función que calcule el promedio de n notas

def calcular_promedio():
    n = int(input("¿Cuantas notas desea promediar?: "))
    if n <= 0: 
        print ("El numero de notas debe ser mayor que 0")
        return None

    notas = []
    for i in range(n):
        nota = float(input (f"Ingresa la nota{i+1}:"))
        notas.append(nota)
    promedio =sum(notas)/ n
    print(f"El promedio de las notas es:{promedio: .2f}")
    return promedio

   
calcular_promedio()

# Cree una función que determine si un color es primario o no

def color_primario (color):

    colores_primarios = ["rojo", "amarillo", "azul"]

    if color in colores_primarios:
        return print(f"el color {color} es primario.")
    else:
        return print(f"el color {color} no es primario.")


color = input ("ingrese un color: ")
resultado = color_primario (color) 

# Cree una función que determine que numero de una serie es mayor.
 
def numero_mayor (numeros):

    mayor = max(numeros)
    return mayor

numeros = []
n = int(input("¿Cuantas numeros desea ingresar?: "))
for i in range(n):
        numero = int(input (f"Ingresa un numero:"))
        numeros.append(numero)       
        
resultado= numero_mayor(numeros)

print (f"el número más grande es {resultado}") 

# Cree una función que dibuje un rectangulo de x filas y columnas

def dibujar_rectangulo (filas, columnas):
    rectangulo=[]

    for i in range (filas):
        if i == 0 or i == filas - 1:
            rectangulo.append("*" * columnas)
        else: rectangulo.append("*" + " " * (columnas - 2) + "*")

    print("\n".join(rectangulo))

fil = int(input("¿Cuantas Filas desea ingresar?: "))
col = int(input("¿Cuantas columnas desea ingresar?: "))

resultado= dibujar_rectangulo(fil,col)

def calcular_factorial (numero):

    factorial = 1
    for i in range(1, numero +1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un numero: "))
resultado = calcular_factorial(numero)
print(f"El Factorial de {numero} es {resultado}")