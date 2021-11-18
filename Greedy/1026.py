n=int(input())
arr=[list(map(int,input().split())) for _ in range(2)]
arr[0].sort()
arr[1].sort(reverse=True)
print(sum(list(map(lambda x,y:x*y,arr[0],arr[1]))))