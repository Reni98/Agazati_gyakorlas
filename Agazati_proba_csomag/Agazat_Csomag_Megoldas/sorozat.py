import random
def lista_letrehoz():
    szamok = []
    for i in range(12):
        szam = random.randint(-10,1000)
        szamok.append(szam)
    return szamok

def lista_kiir(szamok):    
    print("$".join(map(str,szamok)))

def paratlanok_szama(szamok):
    paratlan = 0
    for item in szamok:
        if item % 2 != 0:
            paratlan += 1
    return paratlan

def konzol_kiir(paratlan):
    print(f"A páratlanok száma: {paratlan}")

def fajlba_kiir(paratlan):
    with open("eredmeny.txt", "w", encoding="UTF8") as fajl:
        fajl.write(f"A páratlanok száma: {paratlan}")

l = lista_letrehoz()
k = lista_kiir(l)
p = paratlanok_szama(l)
konzol = konzol_kiir(p)
f = fajlba_kiir(p)