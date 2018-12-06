l=int(input())
if(l%400==0):
    print ("yes")
elif(l%4==0):
    print ("yes")
elif(l%100!=0):
    print ("yes")
else:
    print ("no")
