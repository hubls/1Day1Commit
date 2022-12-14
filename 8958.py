
n = int(input())


for i in range(n):
    s = input()
    total = 0
    c = 0
    for j in range(len(s)):
        if s[j] == 'O':
            c += 1
        elif s[j] == 'X':
            c = 0
        total += c
    print(total)