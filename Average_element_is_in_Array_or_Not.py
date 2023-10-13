n=int(input())
l=list(map(int,input().split()))
a=sum(l)
avg=a//n
print(avg in l)