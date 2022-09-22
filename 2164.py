from collections import deque

n = int(input())

deq = deque(range(1, n+1))


while(1):
    if n == 1:
        print(1)
        break
    
    deq.popleft()
    if len(deq) == 1:
        print(deq[0])
        break
    deq.append(deq[0])
    deq.popleft()
    
