n1 = int(input())
first_lst = list(map(int, input().split()))
n2 = int(input())
second_lst = list(map(int, input().split()))


set1 = set(first_lst)
set2 = set(second_lst)


intersection_lst = set1&set2


for i in range(n2):
    if second_lst[i] in intersection_lst:
        print(1)
    else:
        print(0)
