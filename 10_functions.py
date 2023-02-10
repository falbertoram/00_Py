####################
# Functions
####################

def my_function():
    print("Esto es una funcion")

my_function()


def sum_two_values(val1, val2):
    my_sum = val1 + val2
    return(my_sum)

print(sum_two_values(5,3))


def sumar_two_values (first_number, second_number):
    print(first_number + second_number)

sumar_two_values(5, 5)  # Da como resultado 10
sumar_two_values("5", "5") # Da como resultado 55 porque concatena
                        # los dos strings que pasamos como parametros


def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return (4, 5)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name ("Ramirez", "Alberto")
print_name (surname = "Ramirez", name = "Alberto") # Asignamos valores
                                            # directamente a los parametros
                                            # de la funcion

                                          
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")  # el parametro 'alias' toma
                                    # el valor "Sin alias" por default
                                    # en caso de que en la llamada
                                    # a la funcion no sea pasado
                                    # un valor para ese parametro

print_name_with_default ("James", "Bond", "007")
print_name_with_default ("James", "Bond")


def print_texts (*text):    # Con el * antes del parametro
                        # le indico que me pueden pasar 
                        # uno o mas textos y se imprimiran
                        # todos
    print(text)

print_texts ("Terere", "Mate", "Jugo", 578)


def print_texts_2 (*texts): #Imprime el valor de cada parametro
                        # en una linea distinta
    for text in texts:
        print(text)

print_texts_2 ("GeoPandas", "Pandas", 345, 578)


def print_text_upper (*texts):
    for text in texts:
        print(text.upper())

print_text_upper ("Pandas", "GeoPandas", "TextBlob")


def my_factorial(num_factorial):
    my_fact = 1
    num_iter = num_factorial

    while num_iter > 0: # Factorial de num_fact
        my_fact = my_fact * num_iter
        num_iter -= 1

    return(my_fact)

my_dato = 8
calc_factorial = my_factorial(my_dato)

print(f"El factorial de {my_dato} es: {calc_factorial}")
print("El factorial de {} es: {}".format(my_dato, calc_factorial))
print("El factorial de %d es: %d" %(my_dato, calc_factorial))