import random

def elsoFeladat():
    szam = int(input("Kérlek adj meg egy páros számot: "))
    while not (szam % 2 == 0):
        szam = int(input("Ez nem páros! Kérlek adj meg egy páros számot: "))
    return szam

def masodikFeladat():
    szamlalo = 0
    for i in range(0,13,0):
        szam = random.randint(10,150)
        if szam % 3 == 0:
            szamlalo+1
    print(f"A számok között {szamlalo} darab 3-mal osztható szám van!")