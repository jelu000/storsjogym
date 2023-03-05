import personbil
import lastbil

looping = True

#Initierar 2 st personbils object av classen Personbil
opel_brun = personbil.Personbil("Opel", "Brun", 200)
volvo_svart = personbil.Personbil("Volvo", "Svart", 250)

#Initierar 2 st lastbils object av classen Lastbil
scania_rosa = lastbil.Lastbil("Scania", "Rosa", 40000)
volvobm_orange = lastbil.Lastbil("Volvo BM", "Orange", 50000)

#skapar listor med personbilar och lastbilar
personbils_lista = [opel_brun, volvo_svart]
lastbils_lista = [scania_rosa, volvobm_orange]

#----------------------------------------------
#function som listar valt forton
"""
def print_fordonslista(fordonslista):
    
    for ettfordon in fordonslista:
        #print(ettfordon.fabrikat +" Typ="+ str(type(ettfordon)))
        
        #kollar om ett fordon är en intance av Klassen lastbil eller personbil
        if(isinstance(ettfordon  , lastbil.Lastbil)):
            print(ettfordon.fabrikat +" Färg: "+ ettfordon.color + ", Flakvolym: " + str(ettfordon.flakvolym) +  " L")

        elif(isinstance(ettfordon  ,personbil.Personbil)):
            print(ettfordon.fabrikat +" Färg: "+ ettfordon.color + ", Bagagevolym: " + str(ettfordon.bagagevolym) +  " L")
"""

def print_fordonslista(fordonslista):
    
    for ettfordon in fordonslista:
        ettfordon.print_fordon()



#---------------------------------------------

#main program
while looping:
    print("----------------------------------------")
    print("\n-:Klasser och arv av fordon:-\n")

    val_fordon = input("Vilken fordonstyp vill du lista? 1=lastbilar : 2=personbilar: ")
    

    if (val_fordon == "1"):
        print("\n-:LastBilar:-")
        print("-----------------------------------")
        print_fordonslista(lastbils_lista)
    
    elif (val_fordon == "2"):
        print("\n-:PersonBilar:-")
        print("-----------------------------------")
        print_fordonslista(personbils_lista)

    else:
        print("n\nogiltigt val")

    print("------------------------------------------")
    go = input("\n Vill du lista fordon igen? j/n ")
    print("\n")
    
    if (go == "n"):
        break

