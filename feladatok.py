import random

def elsoFeladat():
    szam = int(input("Kérlek adj meg egy páros számot: "))
    while not (szam % 2 == 0):
        szam = int(input("Ez nem páros! Kérlek adj meg egy páros számot: "))
    return szam

def masodikFeladat():
    szamlalo = 0
    for i in range(0,13,1):
        szam = random.randint(10,150)
        if szam % 3 == 0:
            szamlalo+1
    print(f"A számok között {szamlalo} darab 3-mal osztható szám van!")

def harmadikFeladat(text, N):
    if len(text) < N:
        print("Nincs N. karakter!")
    else:
        karakter = text[N-1].upper()
        print(f"A szöveg {N}-a/o/edik karaktere: {karakter * 3}")
 
def negyedikFeladat():
    nevek = []
    szamlalo = 0
    stoppolo = ""
    while stoppolo != "@":
        stoppolo = str(input("Kérlek adj meg egy nevet (vagy '@' a leállításhoz): "))
        if stoppolo != "@":
            nevek.append(stoppolo)
            szamlalo += 1
    print(f"A felhasználó {szamlalo} nevet adott meg")

def otodikFeladatBekeres():
    felhasznalo_tippje = ""
    while not (felhasznalo_tippje == "kő" or felhasznalo_tippje == "papír" or felhasznalo_tippje == "olló"):
        felhasznalo_tippje = str(input("Kérlek válassz, kő/papír/olló: "))
    felhasznalo_tippje.lower()
    return felhasznalo_tippje

def otodikFeladatGepGeneral():
    gep_tippje = random.randint(1,3)
    if(gep_tippje == 1):
        return "kő"
    elif(gep_tippje == 2):
        return "papír"
    else:
        return "olló"

def otodikFeladatDontes(felhasznalo_tippje:str, gep_tippje:str):
    if felhasznalo_tippje == gep_tippje:
        return "Döntetlen"
    elif (felhasznalo_tippje == "olló" and gep_tippje == "kő"):
        return "A gép győzött"
    elif (felhasznalo_tippje == "papír" and gep_tippje == "olló"):
        return "A gép győzött"
    else:
        return "Az felhasználó győzött"
    
def otodikFeladatKiiras(megoldas):
    print(megoldas)
