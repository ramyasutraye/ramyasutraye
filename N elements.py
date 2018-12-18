try:
 z1=str(input())
 y1=z1.split(" ")
 v=int(y1[1])
 z=str(input())
 y=z.split(" ")
 y.sort(reverse=True)
 print(y[v-1])
except:
 print("Invalid")
