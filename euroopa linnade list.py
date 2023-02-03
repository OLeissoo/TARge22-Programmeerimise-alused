linnad = ["Tallinn", "Helsingi", "Stockholm", "Oslo", "Riia", "Vilnius", "Berlin", "Paris", "Rooma", "Lissabon"]
linnad.append(input("Sisesta 1. linn: "))
linnad.append(input("Sisesta 2. linn: "))
linnadearv = len(linnad)
linnad.sort()
for i in range(linnadearv):
    print(f"{i+1}. {linnad[i]}")
print (f"Meie järjendis on {linnadearv} Euroopa pealinna")