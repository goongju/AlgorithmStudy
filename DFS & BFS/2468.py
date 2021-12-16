n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y):

    if graph[x][y]<=0:
        return False
    graph[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            dfs(nx,ny)
            return True
    return False
result=[]
cnt=0
number=max(map(max, graph))
for k in range(1,number):
#그래프 값 매핑 해야함
    for i in range(n):
        for j in range(n):

            if dfs(i,j)==True:
                cnt+=1
    result.append(cnt)
print(max(result))

