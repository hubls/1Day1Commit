n = int(input())


lst1 = [0] * (n + 1)
lst2 = [0] * (n + 1)

for i in range(n):
    lst1[i+1] = int(input())


if n == 1:
    lst2[1] = lst1[1]

elif n == 2:
    lst2[2] = lst1[1] + lst1[2]

else:
    lst2[1] = lst1[1]
    lst2[2] = lst1[1] + lst1[2]
    lst2[3] = max(lst1[2] + lst1[3], lst1[1] + lst1[3])
    for j in range(4, n+1):
        lst2[j] = max(lst2[j-3]+ lst1[j-1]  + lst1[j] , lst2[j-2] + lst1[j])


print(lst2[n])
