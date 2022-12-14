import sys

n = int(sys.stdin.readline())

lst = set()


for i in range(n):
    s = sys.stdin.readline().strip()

    if ' ' in s :
        command, num = s.split()
        num = int(num)
    else:
        command = s


    if command == 'add':
        lst.add(num)

    elif command == 'remove':
        lst.discard(num)

    elif command == 'check':
        if num in lst:
            print(1)
        else:
            print(0)

    elif command == 'toggle':
        if num in lst:
            lst.discard(num)
        else:
            lst.add(num)

    elif command == 'all':
        lst = set(range(1, 21))

    elif command =='empty':
        lst = set()



