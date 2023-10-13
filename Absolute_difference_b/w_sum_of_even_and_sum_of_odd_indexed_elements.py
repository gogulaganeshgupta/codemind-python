n=int(input())
l=list(map(int,input().split()))
a=sum(l[0:n:2])
b=sum(l[1:n:2])
c=a-b
print(abs(c))