### Sets ###

### Un set es una colección de elementos unicos desordenados ###

# Declarar un set
my_set = set()
print(my_set, type(my_set))

my_other_set = {1, "David", 27, 1.78}
print(my_other_set, type(my_other_set))

# Ver el tamaño de un set
print(len(my_other_set))


# Agregar un nuevo elemento a un set
my_other_set.add("DaroDev")
print(my_other_set)


# Verificar que hay un dato dentro de un set
print("David" in my_other_set)

# Eliminar un elemento de un set
my_other_set.remove("DaroDev")
print(my_other_set)

# Limpiar un set
my_other_set2 = my_other_set.copy()
print(my_other_set2)
my_other_set2.clear()
print(my_other_set2)

# Borrar completamente un set, despues de esto ya no se puede acceder a la misma
del my_other_set2

# Transformar un set en list

my_list = list(my_other_set)
print(my_list, type(my_list))

# Lo anterior nos permite manejar los datos como un list y luego podemos volver a convertirlo en un set

my_set2 = set(my_list)
print(my_set2, type(my_set2))

# Unir dos sets
my_set3 = { "David", 1.78}
my_set4 = {1, 27}

my_set_union = my_set3.union(my_set4)
print(my_set_union)


