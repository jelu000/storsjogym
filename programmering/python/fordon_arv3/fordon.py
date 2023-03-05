#Detta är en bas klass som ska  ärvas av sina barn
class Fordon:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, fabrikat, color):
        self.fabrikat = fabrikat
        self.color = color
        

    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_fabrikat(self, fabrikat):
        self.fabrikat = fabrikat

    def get_fabrikat(self):
        return self.fabrikat
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
