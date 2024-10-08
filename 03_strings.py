### Strings ###

my_variable_string = "Hola Python"
my_other_variable_string = "Hola Python"

print(my_variable_string == my_other_variable_string) # True

print(my_variable_string + " " + my_other_variable_string) # Contatenación de cadenas

my_new_line_string = "Hola\nPython"
print(my_new_line_string) # String con salto de linea

my_string_with_tab = "Hola\tPython"
print(my_string_with_tab) # String con tabulación


### Formateo de strings ###

name, surname, age = "David", "Alonso", 27

print("Mi nombre es %s %s y tengo %s años" %(name, surname, age))
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años") # Python 3.6 en adelante

### Desempaquetado de strings ###
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(f)

### División de strings ###

my_string_for_split = "Hola Python"
my_first_word = my_string_for_split[0:4]
print(my_first_word)


### Darle la vuelta a un string ###

my_string_reversed = my_string_for_split[::-1]
print(my_string_reversed)


### Algunos metodos integrados en strings ###

my_string = "Hola py"

print(my_string.upper()) # Convertir a mayúsculas
print(my_string.lower()) # Convertir a minúsculas
print(my_string.capitalize()) # Convertir la primera letra a mayúscula
print(my_string.replace('py', 'PY')) # Remplazar una cadena por otra 
print(my_string.count('o')) # Contar cuantas veces aparece una letra
print(my_string.startswith('H')) # Comprobar si empieza por una letra
print(my_string.endswith('y')) # Comprobar si termina por una letra
print(my_string.split(' ')) # Dividir una cadena por un caracter
print(my_string.find('a')) # Encontrar la posición de un caracter
print(my_string.index('a')) # Encontrar la posición de un caracter
print(my_string.upper().isupper()) # Comprobar si es mayúscula


