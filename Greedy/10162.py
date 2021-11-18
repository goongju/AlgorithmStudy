n=int(input())
btn=[300,60,10]
result=0
for i,val in enumerate(btn):
    btn[i]=n//val
    result+=1
    n=n%val
if n!=0:
    print(-1)
else:
    print(*btn)