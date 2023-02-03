import random
list = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!", "Sa võid selles kindel olla.", "Suurema tõenäosusega.", "Väljavaated head.", "Märgid viitavad jah-ile.", "Keskendu ja küsi uuesti.", "Ei oska praegu öelda.", "Ära ole selles nii kindel.", "Minu vastus on eitav.", "Minu allikad ütlevad ei.", "Küsi hiljem uuesti", "Pigem praegu ei ütleks.", "Nagu mina näen, jah.", "See on kindel.", "Vastus ähmane, küsi hiljem uuesti.", "Pigem praegu ei ütleks.", "Täiesti kindlasti."]
juhuarv = random.randint(0, 19)

print ("Olen maagiline 8-pall. Võid minult küsida küsimusi ja ma vastan neile.")
vastus = input("Sisesta jah/ei küsimus:")
print (list[juhuarv])

print ("Raputa mind uuesti, kui soovid veel midagi küsida!")