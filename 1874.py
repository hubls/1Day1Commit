n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

basic_lst = list(range(1,n+1))


result = []

temp = []

plus_cnt = 0
basic_cnt = 0

for j in range(2*n):
    if basic_lst[plus_cnt] <= lst[basic_cnt]:
        plus_cnt += 1

