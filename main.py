import feladatok

print("Első Feladat")
feladatok.elsoFeladat()
print("Második Feladat")
feladatok.masodikFeladat()
print("Harmadik Feladat")
feladatok.harmadikFeladat("A majom egy budos lény", 10)
print("Negyedik Feladat")
feladatok.negyedikFeladat()
felhasznalo_tippje = feladatok.otodikFeladatBekeres()
gep_tippje = feladatok.otodikFeladatGepGeneral()
megoldas = feladatok.otodikFeladatDontes(felhasznalo_tippje, gep_tippje)
feladatok.otodikFeladatKiiras(megoldas)