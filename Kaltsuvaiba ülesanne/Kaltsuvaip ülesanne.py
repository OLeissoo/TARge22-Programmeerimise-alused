"""
Rag carpet
"""
def calculate_thread_length(carpet_final_length: float, thread_count: int) -> float:
    single_thread_length = carpet_final_length * 1.2 + 0.5
    return round(single_thread_length * thread_count, 2)

file_name = input("Sisestage failinimi: ")
big_carpet_thread_count = int(input("Sisestage 5-meetrise ja pikemate vaipade lõimede arv: "))
small_carpet_thread_count = float(input ("Sisestage lühemate vaipade lõimede arv: "))

total_length = 0
with open(file_name, "r", encoding="utf-8") as file:
    for row in file:
        carpet_length = float(row)
        if carpet_length >= 5:
            thread_length = calculate_thread_length(carpet_length, big_carpet_thread_count)
        else:
            thread_length = calculate_thread_length(carpet_length, small_carpet_thread_count)
        print(f"{carpet_length} meetrine vaip vajad {thread_length} meetrit lõimeniiti.")
        total_length += thread_length
print(f"Kõikide vaipade peale kokku läheb vaja {total_length:.2f} meetrit lõimeniiti.")
            
            
            