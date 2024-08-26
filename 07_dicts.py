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