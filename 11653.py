input_num = int(input())
temp = input_num

i = 2
lst = []

while(1):
    if input_num % i == 0:
        input_num = input_num//i
        lst.append(i)
    else:
        i +=1

    som = 1
    for l in lst:
        som = som * l

    if som == temp:
        break


for l in lst:
    print(l)
