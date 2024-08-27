### Ciclos o bucles ###

# Los ciclos son una estructura de control que nos permite repetir un bloque de código varias veces.

# While
# El ciclo while ejecuta un bloque de código mientras una condición sea verdadera

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1

print("Fin del ciclo while")

# For
# El ciclo for se utiliza para iterar sobre una secuencia de elementos

my_list = [1,2,3,4,5]

for element in my_list:
    print(element)
    
print("Fin del ciclo for")


# Ciclo while con condicionales

my_number = 12

while my_number > 0:
    if my_number % 2 == 0:
        print("El número "+str(my_number)+" es par")
    else:
        print("El número "+str(my_number)+" es impar")
    my_number -= 1
    
print("Fin del ciclo while con condicionales")


my_dict = {
    "name": "David",
    "age": 27,
    "Height": 1.78
}

for key, value in my_dict.items():
    print(key+": "+str(value))
    
print("Fin del ciclo for con diccionarios")


# For con sets

my_set = {1,2,3,4,5}

for element in my_set:
    print(element)

print("Fin del ciclo for con sets")

# While con break
my_number = 10

while my_number > 0:
    print(my_number)
    my_number -= 1
    if my_number == 5:
        break

print("Fin del ciclo while con break")
 

# Else con ciclos
my_number = 10

while my_number > 0:
    print(my_number)
    my_number -= 1
else: 
    print("Fin del ciclo while con else")
    
my_list = [1,2,3,4,5]

for element in my_list:
    print(element)
else:
    print("Fin del ciclo for con else")
    
