r=input()
r2=str(r.lower())
q=[]
for x in r2:
    if(r2.count(x)==1):
        q.append(x)
r1=" ".join(map(str,q))
print(r1)
