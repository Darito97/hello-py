### Diccionarios ###

# Un diccionario es una colección de datos que se almacenan en pares clave-valor, parecido a un objeto en Javascript.

my_dict = {
    "name": "David",
    "age": 27,
    "height": 1.78,
    "is_developer": True,
    1: 1
}
my_other_dict = dict(name="David", age=27, height=1.78, is_developer=True)
print(my_dict, type(my_dict))
print(my_other_dict, type(my_other_dict))


# Obtener la longitud de pares clave-valor en un diccionario
print(len(my_dict))


# Acceder a uno de los valores por clave
print(my_dict["name"])

# Cambiar el valor de una clave en especifico
my_dict["name"] = "David Alonso"
print(my_dict)

# Agregar un nuevo par clave-valor
my_dict["company"] = "DaroDev"
print(my_dict)

# Eliminar un par clave-valor
del my_dict["company"]
print(my_dict)

# Comprobar un clave en un diccionario
print("name" in my_dict)

# Limpiar un diccionario
my_dict2 = my_dict.copy()
print(my_dict2)
my_dict2.clear()
print(my_dict2)