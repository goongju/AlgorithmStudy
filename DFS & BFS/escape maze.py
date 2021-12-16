from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    for i in range(4):
        nx=x+dx
        ny=y+dy
    while queue:
        if 0<=x<n and 0<=y<m and graph[nx][ny]!=0:
            graph[nx][ny]=graph[x][y]+1
            queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))