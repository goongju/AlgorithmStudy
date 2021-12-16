n,m=map(int, input().split())
graph=[list(map(int,input())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]
queue=[[0,0]]

while queue:
    x,y=queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):

        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                queue.append([nx,ny])
                graph[nx][ny]=graph[x][y]+1
print(graph[n-1][m-1])