##################
# module.py
##################

def sum_valores(number_one, number_two, number_three):
    print(number_one + number_two + number_three)


def factorializar(num_factorial):
    
    my_fact = 1
    num_iter = num_factorial

    while num_iter > 0: # Factorial de num_fact
        my_fact = my_fact * num_iter
        num_iter -= 1

    print(f"El factorial de {num_factorial} es {my_fact}")
    print("El factorial de %d es %d" %(num_factorial, my_fact))
    print("El factorial de {} es {}".format(num_factorial, my_fact))



import math

print(math.pi)
print(math.sin(9))

from math import pi as valor_de_pi

print(valor_de_pi)


