i=0
while(True):
    L,P,V=map(int,input().split())
    if L+P+V==0:
        break
    result=(V//P)*L+min((V%P),L)
    i+=1
    #print('case %d: %d'%(i,result)) 왜 틀렸다고뜨지?
    print("Case {}: {}".format(i, result))