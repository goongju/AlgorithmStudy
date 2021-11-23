T=int(input())
for i in range(T):
    result=1
    n=int(input())
    arr=[tuple(map(int,input().split())) for _ in range(n)]
    arr.sort()
    min=arr[0][1]
    for i in range(len(arr)):
        if arr[i][1]<min:
            min=arr[i][1]
            result+=1
    print(result)

