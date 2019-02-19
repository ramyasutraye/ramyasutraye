n,z=map(int,input().split())
x=0
c=z-1
while(x==0 and c>1):
    if(z%c==0 and n%c==0):
        x+=1
    c-=1
print(c+1)
