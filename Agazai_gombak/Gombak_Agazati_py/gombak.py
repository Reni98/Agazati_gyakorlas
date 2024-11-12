def beolvas(fajlkezeles):
    lista = []
    with open(fajlkezeles, "r", encoding="UTF8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split("@")

            gomba_nev = sor[0]
            nemzetseg =sor[1]
            evszak = sor[2]

            lista.append([gomba_nev, nemzetseg,evszak])
        # for item in lista:
        #     print(f"{item[0]}, {item[1]}, {item[2]}")
    return lista
def gombak_szama(lista):
    print(f"A gombák száma: {len(lista)}")


def papsapka(lista):
    for item in lista:
        if item[1] == "papsapkagombák ":
           nev = item[0]           
           return nev
            
def kiir(nev):
    print(nev)
    

beolv = beolvas("gombak.txt")
szam = gombak_szama(beolv)
p = papsapka(beolv)
k = kiir(p)
