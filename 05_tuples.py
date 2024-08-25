### Tuplas ###


### Como crear una tupla ###

my_tuple = tuple()
print(my_tuple)

other_tuple = ()
print(other_tuple)

my_tuple = (1, "David", 27, 1.78)
print(my_tuple)
print(type(my_tuple))

# Acceder a un elemento de una tupla
print(my_tuple[2])

# Saber cuantos elementos de un dato hay en una tupla
print(my_tuple.count("David"))

# Obtener índice de un elemento
print(my_tuple.index(27))

# Las diferencias entre una lista y una tupla son:
# Las tuplas son inmutables, es decir, no se pueden modificar
# Las tuplas son más rápidas que las listas
# Las tuplas son más seguras que las listas
# Las tuplas son usadas para proteger los datos de la modificación

# Unir tuplas
my_tuple2 = (5,6,7,8)
print(my_tuple + my_tuple2)

# Slice de una tupla
print(my_tuple[0:2])

# Convertir una tupla a lista
my_list = list(my_tuple)
print(my_list, type(my_list))

# Convertir una lista a tupla
my_tuple3 = tuple(my_list)
print(my_tuple3, type(my_tuple3))

# Lo anterior nos sirve para volver a la tupla en determinados casos una lista mutable y 
# luego volverla tupla de nuevo para evitar problemas
