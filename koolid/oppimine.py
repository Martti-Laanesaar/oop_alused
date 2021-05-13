from random import randint

class Andmed():
    def __init__(self, info=):
        if(info is not None):
            self.info = list(info)
        else:
            self.info = []
    def __getitem__(self, i):
        return self.info[i]
    def lisa_info(self, info):
        self.info.append(info)

class Opilane():
    def __init__(self):
        self.nimi = nimi
        self.teadmised = []
    def opib(self, teema):
        self.teadmised.append(teema)

    def unustab(self):
        teema_nr = randint(0, len(self.teadmised))
        print(teema_nr)
        self.teadmised.remove(self.teadmised[teema_nr])


    def kirjeldus(self):
        print("Õpilane " + self.nimi + " teadmised")
        for teema in self.teadmised:
            print(teema)

class Opetaja():
    def opetab(self, teema, *opilane):
        for opilane in opilased:
            opilane.opib(teema)