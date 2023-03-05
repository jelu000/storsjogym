#Detta är en klass som man kan skapa egna Objekt av
class Bil:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_lager(self, lager):
        self.lager = lager

    def get_lager(self):
        return self.lager
    
    def get_fabrikat(self):
        return self.fabrikat
    
    def get_color(self):
        return self.color
    

