#Detta är en klass som ärver fordon och man kan skapa egna Objekt av
import fordon

class Lastbil:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, fabrikat, color, flakvolym):
        self.flakvolym = flakvolym
        self.fabrikat = fabrikat
        self.color = color
        
        
    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym
    
    def print_fordon(self):
        print(self.fabrikat +" Färg: "+ self.color + ", Bagagevolym: " + str(self.flakvolym) +  " L")
    