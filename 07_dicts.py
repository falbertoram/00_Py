######################
# Dictionaries
######################

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name":"James", "Surname":"Bond", "Age":50, 1:"Python"}
print(my_other_dict[1])
print(my_other_dict["Age"])
print(my_other_dict["Surname"])

my_dict = {
    "Name":"James", 
    "Surname":"Bond", 
    "Age":50, 
    "Languages":{"Python", "Matlab", "R"}, # Set
    "Topics":("ChatGPT", "OpenAI", "Tensor Flow"), # Tuple
    "Courses":["Udemy", "Coursera", "Edureka",974], #List
    1:1.72
    }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Name"])
my_dict["Name"] = "Jaime"
print(my_dict["Name"])

my_dict["Address"] = "July, 4th"    # Forma de agregar un nuevo
                                    # campo al diccionario
print(my_dict)

del my_dict["Address"] # Borrar un elemento
print(my_dict)

print(len(my_dict))
my_dict.pop("Courses") # Borrar un elemento
print(my_dict)
print(len(my_dict))

print("Surname" in my_dict)
print("Bond" in my_dict)

my_dict_2 = my_dict.copy()
print(my_dict_2)
print(len(my_dict_2))

print(my_dict.items())
print(type(my_dict.items()))

print(my_dict.keys())

print(my_dict.values())

my_new_dict = dict.fromkeys(("Name", 1, "Piso")) # Crea un nuevo
                                                # diccionario con keys
                                                # pero sin valores
                                                # (todos NONE) 
print(my_new_dict)

my_list = ["Name", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)


my_new_dict = dict.fromkeys(my_dict) # Aqui si tiene sentido usar
                                    # fromkeys porque le estoy 
                                    # pasando como argumento un
                                    # diccionario que ya existe y
                                    # el metodo crea uno nuevo con
                                    # las mismas keys pero con los 
                                    # values seteados a NONE
print(my_new_dict)


my_new_dict = dict.fromkeys(my_dict, "Terere") # Aparte de crear
                                        # un nuevo Dict, tambien
                                        # le asignamos valores a 
                                        # los keys que vinieron de
                                        # my_dict
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Terere", "Termo", 2.22]) 
print(my_new_dict)  # Asignamos una lista de valores
                    # No tiene mucho sentido

my_new_dict = dict.fromkeys(my_dict, ("Terere", "Termo", 2.22)) 
print(my_new_dict)  # Asignamos una tupla de valores
                    # No tiene mucho sentido

my_new_dict = dict.fromkeys(my_dict, {"Terere", "Termo", 2.22}) 
print(my_new_dict)  # Asignamos un set de valores
                    # No tiene mucho sentido


print(list(my_new_dict))    # Cuando al dict lo trasnformamos
                            # en lista, la misma se arma
                            # unicamente con los keys. No
                            # vienen los values. Pasa lo mismo
                            # con tuple y set
                            
print(tuple(my_new_dict))    
print(set(my_new_dict))    

my_values = my_new_dict.values()
print(my_values)

#print(list(dict.fromkeys(list(my_new_dict.values()))))

