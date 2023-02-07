#####################
# LISTS
#####################

my_list = list()    #definimos una lista
my_other_list = []  # otra forma de definir una lista

print(len(my_list))

my_list = [15, 34, 65, 32, 12, 45, 45, 89]
print(my_list)
print(len(my_list))

my_other_list = [50, 1.72, "James", "Bond"]
print(my_other_list)
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1:3])
print(my_other_list[-1])

print(my_other_list.count(50))
print(my_other_list.count("Bond"))

age, height, name, surname = my_other_list
print(surname) 

print(my_list + my_other_list)

my_list_2 = [2, 3, 4]
my_list_3 = list([2, 3, 4, 5])
print(my_list_2)
print(my_list_3)

my_other_list.append("UCA")
print(my_other_list)

my_other_list.insert(1, "Blue")
print(my_other_list)

my_other_list.remove("Blue")
print(my_other_list)

my_list.remove(45) #Hay dos ocurrencias del valor 45, pero solo saca una
print(my_list)

my_list = [15, 34, 65, 32, 12, 45, 89]
print(my_list)
my_list.pop() # Por default, saca el ultimo elemento
#print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(3) # Saca el elemento con indice 3
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina el elemento con indice 2
print(my_list)

my_list.clear()
print(my_list)

my_list = [15, 34, 65, 32, 12, 45, 45, 89]
# my_list.remove(30)  # Si el valor no esta en la lista, 
                    # entonces retorna error
print(my_list)

my_list[2] = "Terere"
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

#print(my_new_list.reverse()) # Retorna None, porque el metodo retorna None

my_new_list.reverse()
print(my_new_list)

my_list = [15, 34, 65, 32, 12, 45, 45, 89]
print(my_list)
my_new_list = my_list[::-1] # Tambien da la vuelta como reverse()
print(my_new_list)

my_new_list.sort()  # No ordena si hay varios data types en la lista
print(my_new_list)



