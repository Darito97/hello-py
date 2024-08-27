### Funciones ###


# Declarar una función
def my_function():
    print("Hola desde mi función")

# Llamar una función
my_function()


# Función con argumentos

def sum(a,b):
    return a+b

# Llamar una función con argumentos

print(sum(2,3))


# Función con argumentos por defecto

def sum2(a=0, b=5):
    return a+b

# Llamar una función con argumentos por defecto

print(sum2(4))
