import requests
import random


#Hämtar giltiga personnummer frå skatteverket 
#Anväder Thunder client för att testa request
#pip install requests
#python.exe -m pip install --upgrade pip

looping = True

while looping:
    slumptal = random.randint(1,3000)
    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={slumptal}&_limit=1"

    #req = requests.get("https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset=200&_limit=1")

    req = requests.get(url)
    json_data = req.json()
    list_results = json_data['results']

    print("\nHär slumpas ett giltigt personnumer från Skatteverket: \n")

    personnummer = list_results[0]['testpersonnummer'] 

    #print(personnummer)
    print(personnummer[2:12])

    entill = input("\nVill du slumpa ett personnummer till? j/n \n")

    if (entill == "n" or entill == "N"):
        break