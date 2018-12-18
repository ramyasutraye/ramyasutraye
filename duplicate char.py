
z = input()
y = [z[0]]
for x in z :
    if x not in y :
        y.append(x)
z2 = ''.join(y)
print(z2)
