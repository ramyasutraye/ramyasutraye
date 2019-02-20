j=int(input())
m=input().split()
b=[]
r=len(m)
for ru in range(0,r):
    q=int(m[ru])
    if(q==ru):
        b.append(ru)
if(len(b)!=0):
    r=' '.join(map(str,b))
    print(r)
else:
    print("-1")
