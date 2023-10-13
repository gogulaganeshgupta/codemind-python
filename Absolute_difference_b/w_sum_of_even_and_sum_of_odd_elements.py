n=int(input())
l=list(map(int,input().split()))
s=0
p=0
for i in l:
    if i%2==0:
        s=s+i
    elif i%2!=0:
        p=p+i
d=s-p
print(abs(d))