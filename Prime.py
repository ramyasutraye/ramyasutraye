q=int(input(""))
r=0
for x in range(1,q+1):
   if(q%x==0):
    r=r+1
if(r==2):
    print("yes")
else:
    print("no")
