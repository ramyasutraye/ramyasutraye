q=int(input())
m=input().split()
b=" ".join(map(str,m))
n=[]
for y in b:
    if(y not in n):
        if(b.count(y)>1):
            n.append(y)
if(len(n)>1):
    m=" ".join(n) 
    i=m[0:1]
    print(i)
else:
    print("unique")
