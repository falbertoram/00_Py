###################
# Strings
###################

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string, my_other_string)

print(my_string, " " + my_other_string)

my_new_line_string = "Mi string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tMi string con tab"
print(my_tab_string)

my_scape_string = "\tMi string con tab \\nand scape"
print(my_scape_string)


#####################
# Formateo
#####################

name, surname, age = "Alberto", "Ramirez", 50
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # sin control de tipo/formato
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # con control de tipo/formato
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # con control de tipo/formato
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # not good practice


################################
# Desempaquetado de caracteres
################################

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

#name, surname = language, language
#print(name, surname)


################################
# Slicing
################################

language_slice = language[2:4]
print(language_slice)

language_slice = language[0:]
print(language_slice)

language_slice = language[-6:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

language_slice = language[-3:-1]
print(language_slice)

language_slice = language[-1]
print(language_slice)

language_slice = language[-1:]
print(language_slice)

language_slice = language[:-1]
print(language_slice)

language_slice = language[:3]
print(language_slice)

############
# Reverse
############

language_slice = language[::-1]
print(language_slice)

language_slice = language[::2] # es lo mismo que el de abajo
print(language_slice)

language_slice = language[0:6:2] # es lo mismo que el de arriba
print(language_slice)

language_slice = language[0:3:2] # es lo mismo que el de arriba
print(language_slice)


##############
# Funciones
##############

language = "python"

print(language.capitalize())
print(language.upper())
print(language.count("h"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))



