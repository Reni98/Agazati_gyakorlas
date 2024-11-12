
def szamBekeres():
    lista = []

    while len(lista)!=5:
        szam = int(input("Adjon meg egy számot(0,120) között: "))
        lista.append(szam)
    print(":".join(map(str,lista)))
    return lista

def elso_idos(lista):
    for i in lista:
        if i > 70:
            index = lista.index(i)    
            return index

def konzolra_ir(index):
    print(f"Első idős ember korának helye a listában: {index}.")

def fajl_ir(index):
    
    with open("oreg.txt", "w", encoding="UTF8") as fajl:
        fajl.write(f"Első idős ember korának helye a listában: {index}.")

korokLista = szamBekeres()
elso = elso_idos(korokLista)
konzol = konzolra_ir(elso)
fajli = fajl_ir(elso)