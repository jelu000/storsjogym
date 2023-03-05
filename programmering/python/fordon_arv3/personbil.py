#Detta är en klass som ärver fordon och man kan skapa egna Objekt av
import fordon

class Personbil:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, fabrikat, color , bagagevolym):
        self.bagagevolym = bagagevolym
        self.fabrikat = fabrikat
        self.color = color
        
        
    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym
    
    def print_fordon(self):
        print(self.fabrikat +" Färg: "+ self.color + ", Bagagevolym: " + str(self.bagagevolym) +  " L")
    