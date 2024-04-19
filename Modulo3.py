#creacion de variables
name = "String" #String
num = 100 #Int
boolean = True #Bool
floates = 10.1 #Float

names_list = ["Andrew", "Fabi", "Pepe"] #list (es posible modificarlo)
names_tuple = ("Andrew", "Fabi") #tuples (no se puede modificar despues)
my_dict = {
    #key : value
    "Nombre" : "Andrew",
    "Apellido" : "Telles",
    "Edad" : 19,
    "Nombre" : "Fabi" #Deberia ser una key única, por lo que va a sobreescribir el valor anterior
} #diccionario

#mostrar variables
print(name) #Devolvera el valor de la variable name
print(num) #Devolvera el valor de la variable num
print(boolean) #Devolvera el valor de la variable boolean
print(floates) #Devoldera el valor de la variable floates

#mostrar listas
print(names_list[2]) #Devolvera un valor exacto de la lista (Pepe)
print(names_tuple[1]) #Devolvera un valor exacto de la tupla (Fabi)

#mostrar diccionario
print(my_dict.get("Apellido")) #Devolvera el value del key Apellido (Telles)
print(my_dict.keys()) #Devolvera todos los keys (Nombre, Apellido, Edad)
print(my_dict.values()) #Devolvera todos los values (Fabi, Telles, 19)

#ejemplo de bucles para el manejo de operadores aritmetico u operadores asignados
x = 0
for x in range(10):
    x += 1 #es lo mismo que x = x + 1
    print(x)

#Ejemplos con condicionales (en un futuro hablaremos a detalle) para dar a entender el uso de operadores relacionales y lógicos
if my_dict.get("Edad") <= 18 and not my_dict.get("Edad") > 12:
    print("Adolescente")
else:
    print("No cumple")

#ejemplo de manejo de acceso de datos (input)
name = input()
"""estoy implementando 2 formas para concatenar texto y variables, 
cualquiera de las 2 formas hace lo mismo, depende de gustos"""
print("Bienvenido usuario " + name + ". Hola")
print(f"Bienvenido persona {name}. Hola")




