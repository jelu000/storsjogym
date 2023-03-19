import random
import sortmodule

#Visar hur en Bubblesort går till

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

listnumbers = []

for tnum in range(5):
    tslumptal = random.randint(0, 100)
    #print(tslumptal)
    listnumbers.append(tslumptal)

print("\n-:SorteringsTest:-")
print("\n-Skriver listnumbers med slumpade tal----------------------------------")
sortmodule.print_set(listnumbers)

print("\n-Sorterar med en gammal BubbelSort--------------------------")
nysorterad_listnumbers = sortmodule.bubble_sort(listnumbers)
sortmodule.print_set(nysorterad_listnumbers)

fortsatt = input("Vill du sortera arrayen igen med Pythons inbyggda functionsort()? j/n ")

if (fortsatt == "j"):
    print("\n-Skriver listnumbers igen----------------------------------")
    sortmodule.print_set(listnumbers)

    print("\n-Sorterar med Pythons sort()----------------------------------")
    listnumbers.sort()
    sortmodule.print_set(listnumbers)


print ("\n Nu är programmet slut!")

