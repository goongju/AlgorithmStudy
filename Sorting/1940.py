n=int(input())
m=int(input())
arr=list(map(int,input().split()))
answer=0
for i in range(len(arr)):
    if m-arr[i] in arr:
        answer+=1
print(int(answer/2))