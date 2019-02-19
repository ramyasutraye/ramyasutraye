z=str(input())
l=[]
for x in range(0,len(z),3):
    l.append(z[x])
r=''.join(map(str,l))
print(r)
