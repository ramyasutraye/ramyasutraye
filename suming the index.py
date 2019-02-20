o,p=map(int,input().split())
q=list(map(int,input().split()))
for r in range(0,p):
    s,t=map(int,input().split())
    u=0
    for v in range(s-1,t):
        u=u+q[v]
    print(u)
