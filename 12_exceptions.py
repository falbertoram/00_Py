##########################
# Exception Handling
##########################


number_one = 5
number_two = 1
number_two = "1"

##### try - except #####

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")


##### try - except - else - finally #####

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except: # No puede haber un try sin un except
    # Se ejecuta si se produce un error
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally: # Opcional
    #Se ejecuta siempre
    print("La ejecucion continua")


##### Excepciones por tipo #####

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: # Se ejecuta solo si se produce un ValueError
    # Se ejecuta si se produce un error
    print("Se ha producido un ValueError")
except TypeError: # Se ejecuta solo si se produce un TypeError
    # Se ejecuta si se produce un error
    print("Se ha producido un TypeError")


##### Captura de la informacion de la excepcion #####

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except TypeError as e: 
    print("WATCH OUT JAMES! " + str(e))
except Exception as e: # Captura cualquier otro tipo de error
                    # que se de distinto a TypeError
    print("WATCH OUT JAMES! " + str(e))

