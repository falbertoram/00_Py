#####################
# Classes
#####################

class My_Empty_Person:    # Camelcase para nombres de clases
    pass    #   

#print(My_Empty_Person)    # Podemos llamar a una clase
#print(My_Empty_Person())  # con o sin parentesis. Los 
                    # parentesis seran necesarios
                    # cuando pasemos parametros


class Person:
    def __init__(self, name, surname):  # Constructor de clase
        self.name = name 
        self.surname = surname
        self.nameeee = name

my_person = Person("James", "Bond")
print(f"{my_person.name} {my_person.surname} {my_person.nameeee}")


class Person222:
    def __init__(self):  # Constructor de clase
                        # sin parametros
        self.name = "James" 
        self.surname = "Bond"

my_person = Person222()
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__ (self, name, surname, alias = "Sin alias"):  # Constructor 
                                                            # de clase
        self.full_name = f"{name} {surname} {alias}" 
        self.__name = name # Para que no pueda ser modificado
                        # por fuera de la clase
        self.__surname = surname  # Para que no pueda ser modificado
                                # por fuera de la clase

    def get_name (self):
        return self.__name  #Puedo retornar desde una funcion pero no
                            # lo puedo modificar publicamente
    
    def walk (self):    # Funciones dentro de clases 
                        # Pasamos 'self' como parametro
                        # para acceder a los elementos de Person
        print(f"{self.full_name} esta caminando")

    

my_person = Person("James", "Bond")
print(my_person.full_name)
my_person.walk()

my_person = Person("James", "Bond", "007")
print(my_person.full_name)
my_person.walk()

my_person.full_name = "Terere" # Cambiamos el valor 
                            #de una propiedad de la clase
print(my_person.full_name)



class Person555:
    def __init__ (self, name, surname, alias = "Sin alias"):  # Constructor 
                                                            # de clase
        self.full_name = f"{name} {surname} {alias}" 
        self.__name = name # Para que no pueda ser modificado
                        # por fuera de la clase
        self.__surname = surname  # Para que no pueda ser modificado
                                # por fuera de la clase

    def get_name (self):
        return self.__name  #Puedo retornar desde una funcion pero no
                            # lo puedo modificar publicamente
    
    def walk (self):    # Funciones dentro de clases 
                        # Pasamos 'self' como parametro
                        # para acceder a los elementos de Person
        print(f"{self.full_name} esta caminando")



my_person = Person555("Jaime", "Bueno")
print(my_person.get_name())
#print(my_person.__surname) # No puedo acceder publicamente
#print(my_person.__name) # No puedo acceder publicamente

my_person.__name = "Testing" # Igual modifica lo que en teoria no
                        # deberia modificar porque al hacerlo
                        # __name deberia bloquear el acceso publico
                        # REVISAR ESTO !!!!!!






