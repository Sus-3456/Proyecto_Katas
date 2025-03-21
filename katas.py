# 1. Función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    # Creo un diccionario para almacenar la entrada
    frecuencia = {}
    # Itero sobre cada letra de la cadena, elimino espacios y convierto a minúsculas
    for letra in cadena.replace(" ", "").lower():
        # Si la letra ya existe en el diccionario, incremento su frecuencia
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            # Si la letra no existe en el diccionario, la inicializo con 1
            frecuencia[letra] = 1
    return frecuencia


# 2. Dada una lista de números, obtengo una nueva lista con el doble de cada valor usando la función map().

def doblar(x):
    return x * 2

# Pido al usuario que ingrese su lista de números separados por comas
entrada_usuario = input("Ingresar lista de numeros separados por comas: ")
# Convierto la entrada en una lista de números enteros
convertir_entrada = list(map(int, entrada_usuario.split(',')))
# Uso map() para aplicar la función doblar a cada valor
result = list(map(doblar, convertir_entrada))

print("Lista con el doble de cada valor: ", result)


# 3. Escribe una función que devuelva una lista con las palabras que contienen una palabra objetivo.

#Ejemplo de lista
lista_palab = input("Escribe que tipo de alimentos comiste hoy seperados por comas: ")
alim_objetivo = 'fruta'

#Funcion
def aliment(lista_palabras, alim_objetivo):
    # Convierto la entrada en una lista de palabras
    lista_palabras = list(map(str, lista_palabras.split(',')))
    for alimento in lista_palabras:
        if alim_objetivo in alimento:
            # Si encuentro la palabra objetivo en alguna, imprimo un mensaje positivo
            print(f"Muy bien! Tu dieta es estupenda")
            return  # Termino la función si encontré la palabra objetivo
    # Si no encuentro la palabra objetivo, imprimo otro mensaje
    print("Oh no! Deberías añadir una pieza de fruta a tu dieta")


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def diferencia(x, y):
    return x - y

# Pido al usuario que ingrese dos listas de num separadsa por comas
lista_1 = input("Primera lista de números (separar por comas): ").split(',')
lista_2 = input("Segunda lista de números (separar por comas): ").split(',')

# Convierto las entradas en listas de num flotantes
lista_1 = list(map(float, lista_1))
lista_2 = list(map(float, lista_2))

# Uso map() para aplicar la función diferencia a cada par de valores de las listas
resultado = list(map(diferencia, lista_1, lista_2))

# MImprimo el resultado
print("La diferencia entre las listas es:", resultado)


# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def aprob(lista_notas, nota_aprobado=5):
    # Calculo la media de las notas
    media = sum(lista_notas) / len(lista_notas)
    # Si la media es mayor o igual a la nota de aprobado, considero que ha aprobado
    if media >= nota_aprobado:
        final = "¡has aprobado! Sigue así"
    else:
        # Si no alcanza la nota de aprobado, el estado es "suspenso"
        final = "has suspendido..."
    return media, final

# Pido al usuario que ingrese sus notas y la nota mínima para aprobar
lista_param = input("¿Qué notas que sacaste? (separadas por comas): ")
nota_aprobado = input("¿Cuál es la nota mínima para aprobar? (valor numérico): ")

# Si el usuario no ingresa una nota de aprobado, le doy un valor por defecto
if nota_aprobado == "":
    nota_aprobado = 5
else:
    nota_aprobado = float(nota_aprobado)

# Convierto las notas a una lista de números flotantes
lista_notas = list(map(float, lista_param.split(',')))

# Llamo a la función y obtengo el resultado
resultado = aprob(lista_notas, nota_aprobado)

# Muestro el resultado
print(f"Tu media es de: {resultado[0]}, por lo que {resultado[1]}")


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    # Si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Si n es mayor que 1, calculo el factorial de n de manera recursiva
        return n * factorial(n - 1)

# Pido al usuario que ingrese un número para calcular su factorial
numero = int(input("Introduce un número para calcular su factorial: "))

# Muestro el resultado
print(f"El factorial de {numero} es {factorial(numero)}")


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tupla_a_string(tupla):
    return f"({tupla[0]}, {tupla[1]})"

# Lista de tuplas de ejemplo
lista_tuplas = [("Perro", 340), ("Gato", 70), ("León", 8), ("Elefante", 3)]

# Uso map() para convertir cada tupla a string
resultado = list(map(tupla_a_string, lista_tuplas))

# Imprimo el resultado
print("Lista de strings:", resultado)


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    # Intento dividir los dos números
    resultado = num1 / num2
    print(f"La división es exitosa. El resultado es: {resultado}")
except ValueError:
    # Si el usuario ingresa algo que no sea un número, manejo el error
    print("Error: Debes introducir números válidos.")
except ZeroDivisionError:
    # Si el usuario intenta dividir por cero, manejo el error
    print("Error: No puedes dividir por cero.")


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtrar_mascotas(mascotas):
    mascotas_proh = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Uso filter() para excluir las mascotas prohibidas
    return list(filter(lambda mascota: mascota not in mascotas_proh, mascotas))

# Pido al usuario que ingrese una lista de mascotas separadas por comas y la convierto en lista
mascotas_input = input("Ingresa una lista de mascotas separadas por comas: ")
mascotas = [mascota.strip() for mascota in mascotas_input.split(',')]

# Obtengo la lista de mascotas permitidas
resultado = filtrar_mascotas(mascotas)

# Imprimo las mascotas permitidas
print("Mascotas permitidas:", resultado)


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista):
    # Si la lista está vacía, lanzo una excepción personalizada
    if not lista:
        raise ListaVaciaError("La lista que añadiste está vacía.")
    # Calculo el promedio si la lista no está vacía
    return sum(lista) / len(lista)

try:
    # Pido al usuario que ingrese números separados por comas
    numeros = [int(x) for x in input("Introduce números separados por comas: ").split(',')]
    # Calculo el promedio de los números
    promedio = calcular_promedio(numeros)
    print("El promedio es:", promedio)
except ListaVaciaError as e:
    # Manejo la excepción si la lista está vacía
    print(e)
except ValueError:
    # Manejo el error si el usuario ingresa algo que no sea un número
    print("Error: Debes introducir valores numéricos.")


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
try:
    # Pido al usuario que ingrese su edad
    edad = int(input("Introduce tu edad: "))
    # Verifico que la edad esté dentro de un rango válido
    if edad < 0:
        print("Estás bien chiquito")
    elif edad > 120:
        print("Usted tiene mucha calle ya")
    else:
        print(f"Tu edad es: {edad}")
except ValueError:
    # Si el usuario ingresa algo que no sea un número
    print("Error: Debes introducir un valor numérico válido.")


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    # Uso map() para obtener la longitud de cada palabra
    return list(map(len, frase.split()))

# Input del usuario
frase = input("Introduce una frase para calcular la longitud de cada palabra: ")

# Obtengo la longitud de cada palabra de la frase
resultado = longitud_palabras(frase)

# Imprimo el resultado
print("Longitudes de las palabras:", resultado)


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def convertir_mayus_minus(caracteres):
    # Uso map() para crear las tuplas de mayúsculas y minúsculas sin letras repetidas
    return list(map(lambda c: (c.upper(), c.lower()), set(caracteres)))


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la función filter().
def palabras_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))

#input de lista de palabras
entrada_palabras = input("Introduce una lista de palabras separadas por comas: ").split(',')
#input de letra en específico
letra = input("Introduce la letra con la que deben comenzar las palabras: ")
# Llamo a la función e imprimo el resutlado
resultado = palabras_por_letra(entrada_palabras, letra)
print(f"14. Palabras que comienzan con la letra '{letra}':", resultado)


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
lista_numeros = input("Introduce una lista de números separados por comas;")
resultado = list(map(lambda x: x + 3, lista_numeros))
print("Adición de 3 unidades a cada número de la lista:", resultado)


# 16. Escribe una función que tome una cadena de texto y un número entero `n` como parámetros y devuelva una lista de todas las palabras que sean más largas que `n`. Usa la función filter().
def palab_larga(frase, n):
    return list(filter(lambda palabra: len(palabra) > n, frase.split()))

# Ejemeplo de usar la función
frase = input("Escribe aquí tu frase: ")
n = int(input("Longitud numérica que marca el límite: "))  # Convertimos a entero
resultado = palab_larga(frase, n)
print(f"Las `palabras más largas que {n} caracteres son:", resultado)


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa la función `reduce()`.

def convert_num(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos) #el primer valor de la lista es la variable x y el segundo es y, y va iterando sobre la lista

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter().
def estudiantes_notaza(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

#Pedir num de estudiantes para iterar sobre ese numero pidiendo información de cada uno y almacenarlo en la lista
num_estudiantes = int(input("¿Cuántos estudiantes hay en total? "))
estudiantes = []

# Pedir datos del usuario usando un bucle for
for i in range(num_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    calificacion = int(input("Calificación: "))
    
    # Crear diccionario y agregarlo a la lista
    estudiantes.append({"nombre": nombre, "edad": edad, "calificacion": calificacion})

resultado = estudiantes_notaza(estudiantes)
print("\nLos estudiantes con calificación mayor o igual a 90 son:")
for est in resultado:
    print(f"- {est['nombre']} (Edad: {est['edad']}, Calificación: {est['calificacion']})")


# 19. Crea una función lambda que filtre los números impares de una lista dada.
numeros = input(int("Escribe la lista numérica separada por comas:"))
resultado = list(filter(lambda x: x % 2 != 0, numeros))
print("Los números impares de la lista dada son:", resultado)


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores `int`. Usa la función `filter()`.
mi_lista = [1, "Tigre", 2, "Gato", 3, "Mapache"]
resultado = list(filter(lambda x: isinstance(x, int), mi_lista))
print("Los valores integer de la lista son:", resultado)


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
numero = input(int("Escribe el número del que quieres calcular el cubo:"))
cubo = (lambda x: x ** 3)(numero)
print("El cubo de", numero, "es:", cubo)


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función `reduce()`.
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Uso de la función
numeros = input(int("Escribe la lista de números separasdos por comas:"))
resultado = producto_total(numeros)
print("El producto total de los valores de la lista dada es:", resultado)


# 23. Concatena una lista de palabras. Usa la función `reduce()`.
def conc_palab(lista_palab):
    return reduce(lambda x, y: x + " " + y, lista_palab)


# 24. Calcula la diferencia total en los valores de una lista. Usa la función `reduce()`.
def dif_total(lista):
    return reduce(lambda x, y: x - y, lista)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_crct(cadena):
    return len(cadena)


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
def resto_division(x, y): # Siendo x e y dos numeros dados
    return x % y

# 27. Crea una función que calcule el promedio de una lista de números.
def calc_avg(lista):
    if not lista:
        raise ValueError("La lista está vacía") #Para cuando de error
    return sum(lista) / len(lista)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_dup(lista):
    vistos = set()
    for num in lista:
        if num in vistos: 
            return num # Si el num está en la lista de vistos devuelve el num
        vistos.add(num) # Si no está en la lista lo añade
    return None  # Si ha pasado por toda la lista y no hay duplicados

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con '#' excepto los últimos cuatro.

def anagramas(palabra1, palabra2):
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return f"'{palabra1}' y '{palabra2}' son anagramas."
    else:
        return f"'{palabra1}' y '{palabra2}' NO son anagramas."

# Inputs del usuario
palabra1 = input("Escribe la primera palabra: ")
palabra2 = input("Escribe la segunda palabra: ")

# Llamar a la función e imprimir el resultado
print(anagramas(palabra1, palabra2))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
def buscar_nombre():
    nombres = input("Introduce los nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_buscar = input("¿Qué nombre quieres buscar? ").strip()
    
    if nombre_buscar in nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_buscar}' NO se encuentra en la lista.")

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto.
def buscar_puesto(nombre, empleados):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre.lower():
            return f"{nombre} es {empleado['puesto']}."
    return f"{nombre} no trabaja aquí o no se encuentra registrado."

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

"""
34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. 
Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.
El objetivo es implementar estos métodos para manipular la estructura del árbol.

Requisitos:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, 
   el número de ramas y las longitudes de las mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
"""

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = [] # Lista vacía para las ramas

    def crecer_tronco(self):
        self.tronco += 1 #Añadir al tronco 1 unidad

    def nueva_rama(self):
        self.ramas.append(1) # Añadir rama al árbol

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas] # Aumental longitud de todas las ramas existentes

    def quitar_ramas(self, posicion):
        if 0 <= posicion < len(self.ramas): #Que la posición no sea negativa
            del self.ramas[posicion] # Eliminar la rama de la posición elegida
        else:
            print(f"No hay una rama en la posición {posicion}.") # En caso de que no exista rama en esa posición

    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de las ramas": self.ramas
        }

# Caso de uso
# 1
arbol = Arbol()
# 2
arbol.crecer_tronco()
# 3
arbol.nueva_rama()
# 4
arbol.crecer_ramas()
# 5
arbol.nueva_rama()
arbol.nueva_rama()
# 6
arbol.quitar_ramas(2)
# 7
print("Información del árbol:", arbol.info_arbol())

"""
36. Crea la clase UsuarioBanco que representa a un usuario de un banco con su nombre, saldo 
y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como 
# retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
"""

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} euros.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} euros. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad} euros.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} euros a {self.nombre}.")
        print(f"Saldo actual de {otro_usuario.nombre}: {otro_usuario.saldo}")
        print(f"Saldo actual de {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad} euros. Saldo actual: {self.saldo}")

# Caso de uso
# 1
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
# 2
bob.agregar_dinero(20)
# 3
bob.transferir_dinero(alicia, 80)
# 4
alicia.retirar_dinero(50)

"""
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
    contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones 
    que tenemos que definir primero y llamar dentro de la función procesar_texto.

Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el reemplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto.
"""

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para un conteo uniforme
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_eliminar]
    return " ".join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) < 2:
            return "Error: Debes proporcionar una palabra_original y una palabra_nueva."
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) < 1:
            return "Error: Debes proporcionar una palabra para eliminar."
        return eliminar_palabra(texto, args[0])
    else:
        return "Error: Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'."

# Caso de uso
texto_prueba = "Hola mundo, que tal anda la peñita."

print("Conteo de palabras:", procesar_texto(texto_prueba, "contar"))

print("Texto con reemplazo:", procesar_texto(texto_prueba, "reemplazar", "mundo", "gente"))

print("Texto sin la palabra 'hermoso':", procesar_texto(texto_prueba, "eliminar", "gente"))

"""
38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
    - Mañana: 6:00 - 11:59
    - Tarde: 12:00 - 18:59
    - Noche: 19:00 - 5:59
"""

def determinar_momento_dia(hora):
    if 6 <= hora <= 11:
        return "Es de mañana."
    elif 12 <= hora <= 18:
        return "Es de tarde."
    elif 19 <= hora <= 23 or 0 <= hora <= 5:
        return "Es de noche."
    else:
        return "Hora no válida. Introduce un valor entre 0 y 23."

# Solicitar hora al usuario
hora_usuario = int(input("Introduce la hora (0-23): "))
print(determinar_momento_dia(hora_usuario))



#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def moment_dia(hora):
    if 6 <= hora <= 11:
        return "Es por la mañana."
    elif 12 <= hora <= 18:
        return "Es por la tarde."
    elif 19 <= hora <= 23 or 0 <= hora <= 5:
        return "Es por la noche."
    else:
        return "Hora no válida. Introduce un valor entre 0 y 23."


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
    #- 0 - 69  → Insuficiente
    #- 70 - 79 → Bien
    #- 80 - 89 → Muy bien
    #- 90 - 100 → Excelente

def calificacion(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación no válida. Introduce un valor entre 0 y 100."


#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos 
# (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio**2
    elif figura == "triangulo":
        base, altura = datos
        return 0.5 * base * altura
    else:
        return "Figura no reconocida."

"""
41. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
después de aplicar un descuento. El programa debe hacer lo siguiente:

1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero).
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
"""

def calcular_precio_final():
    precio = float(input("Introduce el precio original del artículo: €")) # Input del usuario
    tiene_descuento = input("¿Tienes un cupón de descuento? (si/no): ").strip().lower() # Input del usuario
    if tiene_descuento == "si":
        descuento = float(input("Introduce el valor del cupón de descuento (€): "))
        if descuento > 0: # Para que no de error si el valor inicial es cero
            precio_final = precio - descuento
            print(f"¡Descuento aplicado! El precio final es: €{precio_final:.2f}")
        else:
            print("El valor del cupón debe ser mayor a cero.")
            print(f"El precio final es: €{precio:.2f}")
    else:
        print(f"No se aplicó ningún descuento. El precio final es: €{precio:.2f}")



