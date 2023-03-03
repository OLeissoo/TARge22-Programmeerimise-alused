"""
long jump
"""
def adjust_result(faulty_result_m, correction_cm):
    adjusted_result = faulty_result_m + correction_cm / 100
    return adjusted_result
    
file_name = input("Sisesta vigaste tulemuste failinimi: ")
correction = int(input("Sisesta mõõteparandus sentimeetrites: "))
normative = float(input ("Sisesta meistrivõistluste normatiiv meetrites: "))
norm_distances = []
with open(file_name, "r") as file:
    print("Tegelikud tulemused")
    for row in file:
        correct_distance = round(adjust_result(float(row.strip()), correction), 2)
        print(round(correct_distance, 2))
        if correct_distance >= normative:
            norm_distances.append(correct_distance)
print(f"Normatiivi täitis {len(norm_distances)}.")
if len(norm_distances) > 0:
    print(f"Täitnute kesmine on {sum(norm_distances) / len(norm_distances):.2f}")
else:
    print("Normatiivi täitnud puudusid.")