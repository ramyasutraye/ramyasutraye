n=int(input(""))
q=list(map(int,str(n)))
r=list(map(lambda x:x**3,q))
if(sum(r)==n):
    print("yes")
else:
    print("no")
