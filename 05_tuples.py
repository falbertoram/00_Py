#####################
# Tuples
#####################

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (50, 1.72, "James", "Bond")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (90, 60, 90)
print(my_other_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.index(50))
print(my_tuple.count("James"))

# A diferencia de las listas, 
# las tuplas solo tienen como 
# operaciones a "index" y a "count"

#my_tuple[0] = 1.85  # ERROR --> Tuple does not 
                    # support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Convertimos a lista
print(type(my_tuple))

my_tuple[3] = "Bueno"
my_tuple.append("UCA") 
my_tuple.insert(1, "Blue")
print(my_tuple)

my_tuple = tuple(my_tuple) # Lo volvemos a convertir en tupla
print(my_tuple)
print(type(my_tuple))

#del my_tuple
#print(my_tuple) # No se puede hacer print porque el objeto
                # fue borrado en la linea anterior

#del my_tuple[2] # Tuple does not support item deletion