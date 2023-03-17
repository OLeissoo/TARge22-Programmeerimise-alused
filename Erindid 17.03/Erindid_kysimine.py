from Erindid import *
try:
    age,height,weight = AskValues()
except AgeInvalid:
    print("Sisestasid vanuse valesti.")
except HeightInvalid:
    print("Sisestasid pikkuse valesti")
    raise SystemExit
except WeightInvalid:
    print("Sisestasid kaalu valesti")
else:
    print(f"Sinu kehakaaluindeks on: {CalculateBMI(height, weight):.2f}")
