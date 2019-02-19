z,x=map(int,input().split())
d=0
while(z!=0):
    z1=z%10
    if(z1==x):
        d=d+1
    z=int(z/10)
print(d)
