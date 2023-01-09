import sys
from collections import deque


n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
visit_bfs = [0] * (n+1)
visit_dfs = [0] * (n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

for g in graph:
    g.sort()



#dfs
def dfs(v):
    visit_dfs[v] = 1
    print(v, end=' ')
    for nv in graph[v]:
        if visit_dfs[nv] == 0:
            dfs(nv)
dfs(v)
print()


#bfs
Q = deque([v])
visit_bfs[v] = 1
while Q:
    c = Q.popleft()
    print(c, end = ' ')
    for nv in graph[c]:
        if visit_bfs[nv] == 0:
            visit_bfs[nv] = 1
            Q.append(nv)

print()

