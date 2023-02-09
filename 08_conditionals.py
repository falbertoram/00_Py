##########################
# Conditionals
##########################

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 1 * 1

if my_condition == 12:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 y no es igual a 1")


print("La ejecucion continua")

my_string = ""
my_other_string = "fffff"

if my_string: # False si esta vacio y True si no esta vacio
    print("My string no esta vacio")
else:
    print("My string esta vacio")
    

if my_other_string: # False si esta vacio y True si no esta vacio
    print("My other string no esta vacio")
else:
    print("My other string esta vacio")


my_text = ""

if not my_text:  # Operador NOT
    print("My text esta vacio")




