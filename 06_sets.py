###############
# Sets
###############

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"James", "Bond", 50}
print(type(my_other_set))   # Ahora si es un set luego de 
                            # introducir datos en la linea anterior

print(len(my_other_set))

my_other_set.add("Terere") # Set no es una estructura ordenada 
print(my_other_set)

my_other_set.add("Mate") # Set no es una estructura ordenada 
print(my_other_set) 

my_other_set.add("Terere") # Set no admite objetos repetidos 
print(my_other_set) 

#print(my_other_set[0])  # Set is not subscriptable
                        # Esto es logico al no ser una 
                        # estructura ordenada. No sabemos 
                        # en que posicion se guardaran los elementos

print("Bond" in my_other_set) # Comprobar existencia
print("Ramirez" in my_other_set)

my_other_set.remove("Bond")
print(my_other_set)

# Ventaja de Sets: no acepta repetidos y podemos trabajar rapido
# con estructuras que no necesitamos que sean ordenadas

#my_other_set.clear() # Borramos todos los elementos del Set
#print(my_other_set)

#del my_other_set # Eliminamos el objeto
#print(my_other_set)

my_set = {"James", "Bond", 50}
my_list = list(my_set)  # Convertimos a List. Sin embargo, es
                        # un poco arreiagado hacer este tipo de
                        # transformaciones porque no vamos a 
                        # conocer el orden la lista
print(my_list)
print(my_list[0])

my_other_set = {"R", "JavaScript", "Python"}

#my_new_set = my_set + my_other_set  # De esta forma 
                                    # no funciona en Sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_set)) # No pasa nada, siguen
                                                # los mismos elementos 
                                                # porque Set no admite
                                                # repetidos

print(my_new_set.union({"Matlab", "C"}))

print(my_other_set.difference(my_set))

my_set_2 = {"A", "B", "C"}
my_set_3 = {"D", "E", "F"}
print(my_set_2.difference(my_set_3, my_other_set))


                                   

