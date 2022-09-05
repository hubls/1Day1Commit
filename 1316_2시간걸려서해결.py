n = int(input())



lst = []
for i in range(n):
    s = input()
    lst.append(s)


idx = len(lst)
ch = 0

for s in lst:
    if len(s) < 3:
        pass
    
    else:
        t = 1
        for i in range(t, len(s[t:])):
            temp = s[i-1]
            if temp != s[t]:
                val = temp in s[t+1:]
                if val:
                    ch +=1
                    break
            t +=1

print(n - ch)
