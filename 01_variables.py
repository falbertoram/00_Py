# Variables

my_string_variable = "This is my first string" # snake case is the Python convention for variables
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)
print("El valor es:", my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

print('Hello', ',', 'World')

print(len(my_string_variable))

# Variables en una sola linea -- not good practice
name, surename, age, valor = "John", "Dobey", 45, True
print(name, surename, age, valor)

#Person info

person_info = {
    'name1': 'Alberto',
    'surename1': 'Ramirez',
    'surename2': 'Cardozo',
    'age1': 50,
    'bool1': True
}

print(person_info)

# Data entry
first_name = input("What's your name? ")
age = input("How old are you? ")

print(first_name)
print(age)

# Change Data Type
first_name = 50
age = "Alberto"

print(first_name)
print(age)


