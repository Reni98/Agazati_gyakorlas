import random

szam = random.randint(1,51)
print(f"A generált szám: {szam}")
if szam %5 == 0:
    print("A szám öttel osztható!")
elif szam % 3 == 0:
    print("A szám hárommal osztható!")
elif szam % 5 == 0 and szam % 3 == 0:
    print("A szám öttel és hárommal is osztható!")