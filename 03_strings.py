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