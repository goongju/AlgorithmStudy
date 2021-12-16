n,m=map(int,input().split())
arr=list(map(int,input().split()))
#=================================================================
#내가 푼 방식
arr.sort(reverse=True)
for i in reversed(range(arr[0])):
    lst=list(filter(lambda x:x>0,list(map(lambda x:x-i,arr))))
    if sum(lst)>=m:
        print(i)
        break
 #=================================================================

#이진 탐색 방법
start=0
end=max(arr)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in arr:
        if x > mid:
            total+=x-mid
    if total<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)