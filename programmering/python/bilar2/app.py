#Detta är ett program som använder classer och objekt. 
#Det för att lagra flera typer av variabler i de skapade objektet, ide Loke

import bil

looping = True #För att avsluta programmet


volvo_svart = bil.Bil("Volvo", "Svart", 3)
volvo_vit = bil.Bil("Volvo", "Vit", 1)
ferrari_red = bil.Bil("Ferrari", "Röd", 2)

billista = [volvo_svart, volvo_vit, ferrari_red]


print("Första bil= " + billista[0].fabrikat)

while looping:
    print("----------------------------------------")
    print("\n-:BilAutomat:-\n")

    i = 0
    #Skriver ut lista med bilar
    for bil in billista:
        print(str(i+1) + "  :   "+ bil.fabrikat +"  :   "+ bil.color + ",   Antal i lager: " + str(bil.lager) + "st")
        i += 1
    #Slut på lista med bilar
    
    bil_nr = input("\nMata in siffra för vald bil: ")
    #typ omvandlar eller castar string -> int
    bil_nr_int = int(bil_nr)
    #print(bil_nr_int)

    lager_int = billista[bil_nr_int-1].get_lager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print("\nEn " + billista[bil_nr_int-1].color  + "  " + billista[bil_nr_int-1].fabrikat + " kommer här!\n")
        
        #Minskar lager saldo för bilsort
        nytt_lagersaldo_int =  lager_int - 1
        nytt_lagersaldo_string = str(nytt_lagersaldo_int)
        #Minskar lager för bil objektet
        billista[bil_nr_int-1].set_lager(nytt_lagersaldo_int)
    
    else :
        print("\n Tyvärr, slut på! " + billista[bil_nr_int-1].color  + "  " + billista[bil_nr_int-1].fabrikat + "\n")

    print("Lager Saldo före: " + lager_string + " st" )
    print("Lager Saldo efter: " + nytt_lagersaldo_string + " st" )
    print("--------------------------------------------------------\n")

    
    #Avslutar programmet
    go = input("\n Vill du avsluta programmet? j/n ")
    print("\n")
    if (go == "j"):
        break
