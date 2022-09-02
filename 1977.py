import math

a = input()
b = input()
a = int(a)
b = int(b)


#isinstance(math.sqrt(4), int)

lst = []

for i in range(a, b+1):

    if math.sqrt(i).is_integer() == True :
        lst.append(i)


if not lst:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
