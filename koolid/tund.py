from oppimine import *

def menuu():
    print("Tunni programm")
    print("1 - Lisa aine teemad")
    print("2 - Trüki aine teema")
    print("3 - Lisa õpilased klassi")
    print("4 - Õpeta teema õpilastele")
    print("5 - Kontrolli õpilaste teadmised")
    print("6 - Lase õpilasel midagi unustada")
    valik = int(input("Vali sobilik tegevus: "))
    return valik

def lisa_teemad():
    teemad = []
    while(True):
        teema = input("Sisesta teema: ")
        if(teema == ""):
            break
        teemad.lisa_info(teema)
    return teemad

#katsed
valik = menuu()
if(valik == 1):
    aine_teemad = lisa_teemad()
    print("Aine teemad: ")
    for teema in aine_teemad:
        print(teema)
    print("--------------------")



aine_teemad = Andmed("OOP pohimotted", "Klassid ja objektid", "Konstruktor")
print("Aine teemad: ")
for teema in aine_teemad:
    print(teema)
print("--------------------")
kadi = Opilane()
mati = Opilane()
anna = Opetaja()

anna.opetab(aine_teemad[0], kadi, mati)
print(kadi.teadmised)
print(mati.teadmised)

anna.opetab(aine_teemad[1], mati)
print(kadi.teadmised)
print(mati.teadmised)

kadi.kirjeldus()
mati.kirjeldus()

mati.opib(aine_teemad[2])
mati.kirjeldus()