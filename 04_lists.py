### Listas ###

# Ejemplo de definición de una lista
my_list = [1,2,3,4]
print(my_list)

# Otro ejemplo de definición de una lista
my_list = list()
print(my_list)

# Otra forma de definir una lista
my_list = []
print(my_list)

#len nos permite obtener la longitud de una lista
print(len(my_list))
my_list = [1,2,3,4]
print(len(my_list))


# Tipos de datos en una lista
my_list = [27, "David", 1.78]
print(my_list)

# Tipo de dato de una lista
print(type(my_list))

# Acceder a un elemento de la lista
print(my_list[2])

# Si accedemos a un índice negativo, se accede a la lista de derecha a izquierda
print(my_list[-2])

# Saber cuantos elementos de un dato hay en una lista
print(my_list.count("David"))

# Obtener elementos de una lista y asignarles un nombre 
# Para hacer esto se necesita definir nombres para todos los elementos a obtener
age, name, height = my_list
print(age, name, height)


# Unir listas
my_list2 = [5,6,7,8]
print(my_list + my_list2)


# Añadir un elemento
my_list.append("DaroDev")
print(my_list)


