from collections import deque

S = int(input())
N, M = map(int, input().split(' '))

graph = [[0 for j in range(S)] for i in range(S)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    graph[x][y] = 1
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= S or ny <= -1 or ny >= S:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
bfs(N-1, M-1)

for i in graph:
    for j in i:
        print(j, end=' ')
    print()