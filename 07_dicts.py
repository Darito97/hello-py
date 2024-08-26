### Diccionarios ###

# Un diccionario es una colección de datos que se almacenan en pares clave-valor, parecido a un objeto en Javascript.

my_dict = {
    "name": "David",
    "age": 27,
    "height": 1.78,
    "is_developer": True
}
my_other_dict = dict(name="David", age=27, height=1.78, is_developer=True)
print(my_dict, type(my_dict))
print(my_other_dict, type(my_other_dict))
