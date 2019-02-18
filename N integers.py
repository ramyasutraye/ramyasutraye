x=[]
m=int(input(""))
for j in range(1,m+1):
    y=int(input(" "))
    x.append(y)
x.sort()
print("Largest element is:",x[m-1])
