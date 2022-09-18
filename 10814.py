import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    age, s = sys.stdin.readline().rstrip().split()
    temp = [int(age), s]
    lst.append(temp)


lst.sort(key = lambda x: x[0])



for i in range(n):
    print(lst[i][0], lst[i][1])
