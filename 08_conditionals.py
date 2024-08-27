### Condicionales ###

# Condicional

my_condition = True

if my_condition:
    print("La condición es verdadera")


print("Fin de la condición")


# Condicional if con else

my_condition = False

if my_condition:
    print("La condición es verdadera")
else:
    print("La condición es falsa")
    
print("Fin de la condición if-else")


# Condicional con igualación
my_number = 15

if my_number == 15:
    print("El número es 15")
else:
    print("El número no es 15")

print("Fin de la condición de igualación")

# Condicional con diferente

my_number = -15

if my_number != 15:
    print("El número no es 15")
else:
    print("El número es 15")

print("Fin de la condición de diferente")


# Condicional con and

my_number = 15

if my_number > 0 and my_number == 15:
    print("El número es mayor que 0 y es 15")
else:
    print("El número no es mayor que 0 o no es 15")

print("Fin de la condición de and")

# Condicional con or
my_number = -15

if my_number < 0 or my_number == 15:
    print("El número es menor que 0 o es 15")
else:
    print("El número no es menor que 0 o no es 15")
    
print("Fin de la condición de or")


# Condicional if con elif y else

my_number = 15

if my_number < 0:
    print("El número es menor que 0")
elif my_number == 0:
    print("El número es 0")
elif my_number == 15:
    print("El número es 15")
else:
    print("El número es mayor que 0, diferente de 0 y diferente de 15")

print("Fin de la condición if-elif-else")


