z,y=input().split()
y=int(y)
x=len(z)
w=[]
for j in range(0,x):
	r=z[j]
	w.append(r)
d=x-y
a=[]
for j in range(y,x):
	r=w[j]
	a.append(r)
print("".join(a))
