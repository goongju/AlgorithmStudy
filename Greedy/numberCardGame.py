n,m=map(int,input().split())
arr=[0 for i in range(n)]
for i in range(n):
    data=list(map(int,input().split()))
    arr[i]=min(data)
print(max(arr))