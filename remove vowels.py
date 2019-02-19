z=input(" ")
vowels=('a','e','i','o','u')
for x in z.lower():
    if x in vowels:
        z=z.replace(x,"")
print(z[::-1])
