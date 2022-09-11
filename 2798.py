from itertools import combinations


n, m = input().split()
m = int(m)

lst = list(map(int, input().split()))



big_num = 0

for i in combinations(lst, 3):
    temp_sum = sum(i)

    if big_num < temp_sum <= m:
        big_num = temp_sum

print(big_num)





'''
max_lst.sort()

for i in range(len(max_lst)):
    
    if max_lst[i] > m :
        print(max_lst[i-1])
        break
    

'''
