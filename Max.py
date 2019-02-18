z=int(input())
y=[]
y=list(map(int,input().split()))
s1=y[::2]
s2=y[1::2]
s3=y[1::3]
if(sum(s1)>sum(s2) and sum(s1)>sum(s3)):
  print(sum(s1))
elif(sum(s3)>sum(s1) and sum(s3)>sum(s2)):
  print(sum(s3))
else:
    print(sum(s2))
