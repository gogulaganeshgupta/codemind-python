n=int(input())
if n%2!=0:
    print("weird")
elif n>=2 and n<=5 and n%2==0:
    print("not weird")
elif n>=6 and n<=20 and n%2==0:
    print("weird")
else:
    print("not weird")