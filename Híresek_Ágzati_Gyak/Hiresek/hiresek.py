lista=[]

for i in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    fogalkozas = input("Add meg a foglalkozását!")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)!")
    lista.append([nev,fogalkozas,nemzetiseg])

with open("hiresnok.txt", "w", encoding="UTF8") as fajl:

    for list in lista:
        if list[2] == "a":
            fajl.write(f"Ms.{list[0]}egy híres {list[1]}")
        else:
            fajl.write(f"Frau {list[0]}egy híres {list[1]}")