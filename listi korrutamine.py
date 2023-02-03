list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tegur = int(input("Sisesta arv: "))
for i in list:
    print(f"{tegur} * {list[i-1]} = {tegur * int(list[i-1])}")