szam1 = int(input("Adj meg egy számot!"))
szam2 = int(input("Adj meg egy másik számot!"))

if szam1 > szam2:
   print(f"A nagyobb érték {szam1}")
elif szam2 > szam1:
    print(f"A nagyobb érték {szam2}")
else:
    print(f"A két szám egyenlő")