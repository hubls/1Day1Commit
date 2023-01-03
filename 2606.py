from collections import deque
'''
x = input()
n = int(input())

lst = [[]]

for i in range(n):
    tmp = list(map(int, input().split()))
    lst.append(tmp)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    print(queue)

    while queue:
        v = queue.popleft()
        print(v, end = '')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * n

bfs(lst, 1, visited)

'''

#dfs 풀이방식
'''
n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)]
visit = [0] * (n+1)


for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):
    visit[v] = 1
    for nv in graph[v]:
        if visit[nv] == 0 :
            dfs(nv)

dfs(1)
print(sum(visit)-1)
'''



#BFS 풀이방식

from collections import deque

n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수

graph = [[] for i in range(n+1)]
visit =[0] * (n+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visit[1] = 1
Q = deque([1])

print(graph)

while Q:
    print(Q)
    c = Q.popleft()
    for nx in graph[c]:
        if visit[nx] == 0:
            Q.append(nx)
            visit[nx] = 1


print(visit)
