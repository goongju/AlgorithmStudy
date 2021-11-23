s=input()
a=s.split('0')
b=s.split('1')

print(min(len(' '.join(a).split()),len(' '.join(b).split())))