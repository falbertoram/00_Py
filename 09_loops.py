##################
# Loops
##################

############### While ###############

my_condition = 0

while my_condition < 10:
    print(my_condition)
    if my_condition == 5:
        print("Se detiene la ejecucion")
        break

    my_condition += 1

else:   # En Python al While se le puede poner un else
    print("La condicion es mayor o igual que 10")

print("La ejecucion continua")


num_factorial = 8
my_fact = 1
num_iter = num_factorial

while num_iter > 0: # Factorial de num_fact
    my_fact = my_fact * num_iter
    num_iter -= 1

print(f"El factorial de {num_factorial} es {my_fact}")
print("El factorial de %d es %d" %(num_factorial, my_fact))
print("El factorial de {} es {}".format(num_factorial, my_fact))


############### For ###############

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)


my_tuple = (50, 1.72, "James", "Bond")

for element in my_tuple:
    print(element)


my_set = {"James", "Bond", 50}

for element in my_set:
    print(element)


my_dict = {"Name":"James", "Surname":"Bond", "Age":50, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Age":
        print("Llegamos al elemento AGE y hacemos break")
        break   # sale del loop

for element in list(my_dict.values()):
    print(element)
    
for element in my_dict.values():
    print(element)
else:   # En Python al While se le puede poner un else
    print("El for loop para my_dict ha finalizado")

for element in my_dict:
    print(element)
    if element == "Age":
        continue # Hace un break en esta parte del loop 
                # y vuelve al inicio del for
    print("Se ejecuta")
else:
    print("El for loop para my_dict ha finalizado")
    