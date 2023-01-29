n = int(input())

lst = []
answer_lst = []
count = 1
flag = 0

for i in range(n):
    num = int(input())

    while count <= num :

        lst.append(count)
        answer_lst.append('+')
        count += 1

    if lst[-1] == num :
        lst.pop()
        answer_lst.append('-')

    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for idx in answer_lst:
        print(idx)







