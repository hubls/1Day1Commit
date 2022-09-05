n = int(input())


line = 0
max_num = 0

while (max_num < n):
    line += 1
    max_num += line

gap = max_num - n


if line % 2 == 0:
    top = line - gap
    bottom = max_num - n + 1
    print(str(top)+"/"+str(bottom))


else:
    top = gap + 1
    bottom = line - gap
    print(str(top)+"/"+str(bottom))



