z=int(input())
y=input().split()
w=len(y)
for j in range(0,w):
	a=y.count(y[j])
	if (a<2):
		print(y[j])
