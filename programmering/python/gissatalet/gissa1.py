import random

print("\nGissa Talet\n")

print("Gissa ett tal mellan 1-10, du har 3 st försök!")
slumptal = random.randrange(1, 10)
i=1
vinst = False
print(slumptal)
while  i<4:
    gissattal = input("Skriv in ett tal: ")
    i = i+1

    if slumptal==int(gissattal):
        print("\nGrattis du har vunnit en anka\n")
        vinst = True
        break
    
if vinst==False:
    print("\nDe blev ingen Anka\n")
