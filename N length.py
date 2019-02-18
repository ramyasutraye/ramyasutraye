z=input()
y=input()
start = 0
while start < min(len(z), len(y)):
    if z[start] != y[start]:
        break
    start += 1
print(z[:start])
