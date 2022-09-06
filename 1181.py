n = int(input())
lst = []

for i in range(n):
    word = input()
    lst.append((word, len(word)))
    
setlst = set(lst)

lenlst = sorted(list(setlst), key = lambda x: (x[1], x[0]))
for s, l in lenlst:
    print(s)
