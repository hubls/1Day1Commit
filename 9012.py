n = int(input())

for i in range(n):
    str_ = input()
    
    lst = []
    x = 0
    for s in str_:        
        if s == '(' :
            lst.append(s)
        
        else:
            try:
                lst.pop()
            except:
                x = 1
                break
        

    if len(lst) == 0 and x==0 :
        print("YES")

    else:
        print("NO")
