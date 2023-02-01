import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))

    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return




n = int(sys.stdin.readline())

for i in range(n):
    m, n, k = map(int, sys.stdin.readline().split())
    cnt = 0
    graph = [[0] * n for i in range(m)]

    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)