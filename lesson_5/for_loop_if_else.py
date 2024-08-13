# for loop and if/else priklad

def je_cislo_liche(cislo):
    podil = int(cislo/2)
    zbytek = cislo - 2*podil
    return zbytek

for i in range(0,5):
    if je_cislo_liche(i):
        print(str(i) + " je liche")
    else:
        print(str(i) + " je sude")

