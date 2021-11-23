n=int(input())
road=list(map(int,input().split()))
price=list(map(int,input().split()))

min=price[0]
result=0
for i in range(n-1):
    if price[i]<min:
        min=price[i]
    result+=min*road[i]
print(result)