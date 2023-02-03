arv = [1, 2, 3, 4]
eesti = ["üks", "kaks", "kolm", "neli"]
inglise = ["one", "two", "three", "four"]
itaalia = ["uno", "due", "tre", "quattro"]

arv.sort()
eesti.sort()
inglise.sort()
itaalia.sort()

abiarv = 0

arv.append(5)
eesti.append("viis")
arv.append(6)
eesti.append("kuus")

for number in arv:
    print(number,"-", eesti[number-1], "-", inglise[abiarv], "-", itaalia[abiarv])
    if abiarv <= 2:
        abiarv += 1
if "tre" in itaalia:
    print("Järjendis itaalia on sõna 'tre'.")