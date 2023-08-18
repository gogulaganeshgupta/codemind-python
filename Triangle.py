s1,s2,s3=map(int,input().split())
if s1==s2 and s2==s3 and s3==s1:
    print("Equilateral triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")