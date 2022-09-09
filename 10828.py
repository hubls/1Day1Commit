import sys

n = int(input())
lst = []


'''
class Stack:
    def __init__(self):
        self.top = []

    def __len__(self) -> bool :
        return len(self.pop)

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print(-1)
    def

'''
for i in range(n):
    s = sys.stdin.readline()
    if (s[:2] == 'pu'):
        lst.append(int(s[5:]))
    elif (s[:2] == 'po'):
        if len(lst) == 0 :
            print(-1)
        else:
            print(lst.pop())
    elif (s[:2] == 'si'):
        print(len(lst))

    elif s[:2] == 'em' :
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif s[:2] == 'to':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])      

    
