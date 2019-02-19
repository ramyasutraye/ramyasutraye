z1,n=map(int,input().split())
z=input().split()
while(n>0):
    z.insert(0,z.pop())
    n=n-1
for j in range(0,len(z)):
    if(j!=len(z)-1):
        print(z[j],end=(" "))
    else:
        print(z[j])
