import sys

n = int(input())
lst = []

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push_front':
        lst.insert(0, int(s[1]))
        
    elif s[0] == 'push_back':
        lst.append(int(s[1]))
        
    elif  s[0] == 'pop_front':
        if lst:
            print(lst[0])
            del lst[0]
        else:
            print(-1)
            
    elif s[0] == 'pop_back':
        if lst:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
            
    elif s[0] == 'size':
        print(len(lst))
        
    elif s[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)

    elif s[0] == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)

    elif s[0] == 'back':
        if lst:
            print(lst[-1])
        else:
            print(-1)

