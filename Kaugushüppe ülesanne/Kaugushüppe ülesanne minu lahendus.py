"""
long jump
"""
def adjust_result(faulty_result_m, correction_cm):
    adjusted_result = faulty_result_m + correction_cm / 100
    return adjusted_result
    
file_name = input("Sisesta vigaste tulemuste failinimi: ")
correction = int(input("Sisesta mõõteparandus sentimeetrites: "))
normative = float(input ("Sisesta meistrivõistluste normatiiv meetrites: "))
normative_success = 0
normative_avg = 0
with open(file_name, "r") as file:
    print("Tegelikud tulemused")
    for row in file:
        if round(adjust_result(float(row.strip()), correction), 2) > normative:
            normative_success += 1
            normative_avg += round(adjust_result(float(row.strip()), correction), 2)
        print(round(adjust_result(float(row.strip()), correction), 2))
print(f"Normatiivi täitis {normative_success}")
if (normative_success) > 0:
    normatiivkeskmine = round((normative_avg / normative_success),2)
    print(f"Täitnute keskmine on {normatiivkeskmine}.")

