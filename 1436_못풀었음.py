import sys

s_num = '666'
num = int(input())
lst = []

if num < 7:
    fnum = int(str(num - 1) + s_num)
    print(fnum)
    sys.exit()

for i in range(num - 6):
    int(s_num + str(i + 1))




    #a1 = int(str(i) + s_num)
    #a2 = int(s_num + str(i))
