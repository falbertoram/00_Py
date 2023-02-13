#####################
# Modules
#####################

# Para poder acceder a un archivo como modulo, el mismo
# no debe empezar con numero. Se ve esto al intentar importar
# 10_functions.py por ejemplo

import my_module # Importa todos los elementos de my_module

my_module.sum_valores(4,3,3)
my_module.factorializar(10)


# Importar solo uno o mas elementos de my_module
from my_module import sum_valores
from my_module import sum_valores, factorializar

sum_valores(5, 3, 1)
factorializar(8)
