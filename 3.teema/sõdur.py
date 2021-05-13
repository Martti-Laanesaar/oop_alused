from Inimene import Inimene

class Sõdur(Inimene):
    #konstruktor
    def __init__(self, an):
        super().__init__()
        self.armee_nr = an