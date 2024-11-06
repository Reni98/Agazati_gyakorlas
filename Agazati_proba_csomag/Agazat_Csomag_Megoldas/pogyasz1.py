def beolvas(fajkezeles):
    lista = []
    with open(fajkezeles, "r", encoding="UTF8") as file:
        lines = file.readlines()

        for line in lines[1:]:
            line = line.strip()
            adat = line.split("#")

            szelesseg = int(adat[0])
            magassag = int(adat[1])
            melyseg = int(adat[2])
            suly = int(adat[3])
            lista.append([szelesseg, magassag,melyseg,suly])
        return lista
           
        # for item in lista:
        #     print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")

def pogyaszok_szama(lista):
    print(f"A pogyászok száma: {len(lista)}")

def atlag(lista):
    sulyok = []
    for item in lista:
        if item[0] == 51:
            sulyok.append(item[3])
    print(sulyok)
    print(f"Az 51 cm-es pogyászok átlag súlyértéke: {round((sum(sulyok)/len(sulyok))* 1000)} g")

def legmagasabb_pogyasz(lista):
    legmagasabb = 0
    legszelesseg = 0
    legmelyseg = 0
    legsuly = 0
    for item in lista:
        if item[1] > legmagasabb:
            legmagasabb = item[1]
            legszelesseg = item[0]
            legmelyseg = item[2]
            legsuly = item[3]
    print(f"A legmagasabb pogyász méretei: {legszelesseg} x {legmagasabb} x {legmelyseg}, súlya: {legsuly} kg ")


beolv = beolvas("csomag.txt")
pogy_szam = pogyaszok_szama(beolv)
a = atlag(beolv)
leg = legmagasabb_pogyasz(beolv)