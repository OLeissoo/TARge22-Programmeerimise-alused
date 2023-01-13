list = [2, 4, 8]

for number in list:
    print(number)
    number=number * 3
    
for i in range(len(list)):
    list[i] = list[i] * 3

for number in list:
    print(number)