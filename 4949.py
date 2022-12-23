
while True :
    sentence = input()
    lst = []
    if sentence == '.' :
        break

    for i in range(len(sentence)):
        try:
            if sentence[i] == '(':
                lst.append('(')
            elif sentence[i] == '[':
                lst.append('[')
            elif sentence[i] == ')':
                temp = lst.pop()
                if temp == '(':
                    pass
                else:
                    lst.append([100, 200, 300])

            elif sentence[i] == ']':
                temp = lst.pop()
                if temp == '[':
                    pass
                else:
                    lst.append([100,200,300])
        except:
            lst.append([100, 200, 300])

    if len(lst) == 0 :
        print('yes')
    else:
        print('no')
