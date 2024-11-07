def bekeres():
    szam = int(input("Kérlek adj meg egy páros számot: "))
    while not (szam % 2 == 0):
        szam = int(input("Ez nem páros! Kérlek adj meg egy páros számot: "))
    return szam
