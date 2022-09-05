input_str = input()

i = 0
idx = 0
while (i < len(input_str)):

    if i == len(input_str) -1:
        i +=1
        idx += 1
        break
    
    if input_str[i] == 'c' :
        if input_str[i+1] == '=' or input_str[i+1] == '-':
            i +=2
            idx += 1
            continue
    elif input_str[i] == 'd':
        if input_str[i+1] == 'z' and i < len(input_str)-2 :
            if input_str[i+2] == '=':
                i +=3
                idx += 1
                continue
        elif input_str[i+1] == '-':
            i += 2
            idx += 1
            continue
           
    elif input_str == '-' :
            i += 2
            idx += 1
            continue
    elif input_str[i] == 'l':
        if input_str[i+1] == 'j':
            i += 2
            idx += 1
            continue
    elif input_str[i] == 'n':
        if input_str[i+1] == 'j':
            i += 2
            idx += 1
            continue
    elif input_str[i] == 's':
        if input_str[i+1] == '=':
            i += 2
            idx += 1
            continue
    elif input_str[i] == 'z':
        if input_str[i+1] == '=':
            i += 2
            idx += 1
            continue
    i +=1
    idx += 1


print(idx)    

