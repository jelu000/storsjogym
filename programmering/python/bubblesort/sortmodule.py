#Visar hur en BubbleSort går till
def bubble_sort(tset):
    
    tlist = tset.copy()

    langd = len(tlist)



    bytplats = False

    for i in range(langd-1):
        
        for j in range(0, langd-i-1):

            if tlist[j] > tlist[j + 1]:
                bytplats = True
                tlist[j], tlist[j + 1] = tlist[j + 1], tlist[j]

        if not bytplats:
            return

    return tlist

def print_set(tlist):

    langd = len(tlist)
    langd = 10
    for tal in tlist:
        print(tal)


