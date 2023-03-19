#1. Denna uppgift ska man öva variabler, vilkor och loopar
import random
print("\n-----------------------------------------------------------")
print(".:GissaTalet:.\n\n")

print("gissa ett tal mellan 1 och 10 och pröva lyckan, du får 3st försök!\n")
slumptal = random.randrange(1, 10)
#print(slumptal)
i = 0
hittat = False

while i < 3:
    gissatal =input("mata in tal: " )
    
    if slumptal == int(gissatal):
        hittat = True
        print("\n rätt svar! \n")
        break
    
    i += 1

if hittat:
    print("\nBra jobbat, här får du fem spänn")
else:
    print("\nBättre lycka nästa gång")

print("\n-----------------------------------------------------------")